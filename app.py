import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Ändere dies in einen sicheren Schlüssel

logging.basicConfig(level=logging.DEBUG)

# Flask-Login Konfiguration
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Dummy Benutzer
users = {'admin': {'password': 'password123'}}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    ssid, password = read_hotspot_settings()
    hostname = read_hostname()
    logging.debug(f"SSID: {ssid}, Password: {password}, Hostname: {hostname}")  # Protokolliere die gelesenen Werte
    return render_template('index.html', ssid=ssid, password=password, hostname=hostname)

@app.route('/update_settings', methods=['POST'])
@login_required
def update_settings():
    ssid = request.form['ssid']
    password = request.form['password']
    hostname = request.form['hostname']
    update_hotspot_settings(ssid, password)
    update_hostname(hostname)
    return redirect(url_for('index'))

def read_hotspot_settings():
    config_path = '/etc/NetworkManager/system-connections/Hotspot.nmconnection'
    ssid = ''
    password = ''
    try:
        with open(config_path, 'r') as f:
            for line in f:
                logging.debug(f"Reading line: {line.strip()}")  # Protokolliere jede Zeile
                if line.strip().startswith('ssid='):
                    ssid = line.split('=')[1].strip()
                    logging.debug(f"Found SSID: {ssid}")  # Protokolliere gefundene SSID
                if line.strip().startswith('psk='):
                    password = line.split('=')[1].strip()
                    logging.debug(f"Found Password: {password}")  # Protokolliere gefundenes Passwort
    except Exception as e:
        logging.error(f'Error reading configuration: {e}')
    logging.debug(f'Read SSID: {ssid}, Read Password: {password}')  # Protokolliere die gelesenen Werte
    return ssid, password

def update_hotspot_settings(ssid, password):
    config_content = f"""
    [connection]
    id=Hotspot
    uuid=39785851-0780-430b-a057-72cd6f657d9a
    type=wifi
    autoconnect=false
    interface-name=wlp4s0
    permissions=
    timestamp=1717787614
    autoconnect=true

    [wifi]
    mac-address-blacklist=
    mode=ap
    seen-bssids=C8:8A:9A:FA:9B:8C;
    ssid={ssid}

    [wifi-security]
    group=ccmp;
    key-mgmt=wpa-psk
    pairwise=ccmp;
    proto=rsn;
    psk={password}

    [ipv4]
    dns-search=
    method=shared

    [ipv6]
    addr-gen-mode=stable-privacy
    dns-search=
    method=auto

    [proxy]
    """
    config_path = '/etc/NetworkManager/system-connections/Hotspot.nmconnection'
    with open(config_path, 'w') as f:
        f.write(config_content.strip())
    logging.debug(f'Updated configuration: {config_content.strip()}')
    os.system('sudo chmod 600 ' + config_path)
    os.system('sudo systemctl restart NetworkManager')
    logging.debug('Restarted NetworkManager')

def read_hostname():
    try:
        with open('/etc/hostname', 'r') as f:
            hostname = f.read().strip()
            logging.debug(f'Read Hostname: {hostname}')
            return hostname
    except Exception as e:
        logging.error(f'Error reading hostname: {e}')
        return ''

def update_hostname(hostname):
    try:
        with open('/etc/hostname', 'w') as f:
            f.write(hostname + '\n')
        logging.debug(f'Updated Hostname: {hostname}')
        os.system('sudo hostnamectl set-hostname ' + hostname)
    except Exception as e:
        logging.error(f'Error updating hostname: {e}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)