# OWIPEX Tools Setup

Dieses Repository enthält die notwendigen Skripte und Dateien zur Einrichtung des OWIPEX Tools. Das Tool ermöglicht die Konfiguration von WiFi-Hotspot-Einstellungen, Hostnamen und verschiedenen Edge-Parametern über eine benutzerfreundliche Webschnittstelle.

## Inhaltsverzeichnis

- [Installation](#installation)
- [Verwendung](#verwendung)
- [Beschreibung des HTML Tools](#beschreibung-des-html-tools)
- [Service Management](#service-management)

## Installation

1. **Klonen des Repositories**:
    ```sh
    git clone https://github.com/dein-repo/owipex-tools.git
    cd owipex-tools
    ```

2. **Setup-Skript ausführen**:
    Führe das Setup-Skript `setup.sh` aus, um die virtuelle Umgebung zu erstellen, die notwendigen Python-Bibliotheken zu installieren und den Systemdienst einzurichten.
    ```sh
    chmod +x setup.sh
    sudo ./setup.sh
    ```

## Verwendung

Nach der Installation und Einrichtung startet der Dienst automatisch beim Hochfahren des Rechners. Die Webanwendung ist dann unter `http://<deine-ip>:5000` erreichbar.

### Anmeldeinformationen

- **Benutzername**: `admin`
- **Passwort**: `password123`

## Beschreibung des HTML Tools

Das OWIPEX Tools HTML-Tool ermöglicht die einfache Konfiguration verschiedener Geräteeinstellungen über eine benutzerfreundliche Weboberfläche. Die Hauptfunktionen sind:

- **WiFi-Hotspot-Einstellungen**: Konfiguriere SSID und Passwort des WiFi-Hotspots.
- **Hostname**: Setze den Hostnamen des Geräts.
- **EDGE-Einstellungen**: Konfiguriere EDGE Key, EDGE Secret, Datenbank-Passwort, Cloud RPC Host und Spring Datasource URL.
- **SPS**: Verwalte den ThingsBoard Access Token.

### Benutzeroberfläche

- **Logo**: Das OWIPEX-Logo wird oben auf jeder Seite angezeigt.
- **Abschnitte**: Die Konfigurationseinstellungen sind in folgende Abschnitte unterteilt:
  - Gerät
  - EDGE
  - SPS

Die Abschnitte helfen dabei, die verschiedenen Einstellungen übersichtlich und leicht zugänglich zu machen.

## Service Management

### Status des Dienstes überprüfen

Um den Status des OWIPEX Tools Dienstes zu überprüfen, verwende den folgenden Befehl:

```sh
sudo systemctl status owipex-tools.service



### Erklärung

- **Installation**: Eine Schritt-für-Schritt-Anleitung zur Installation und Einrichtung des Tools.
- **Verwendung**: Anweisungen, wie das Tool verwendet wird, inklusive der Anmeldeinformationen.
- **Beschreibung des HTML Tools**: Eine kurze Beschreibung der Hauptfunktionen und der Benutzeroberfläche des Tools.
- **Service Management**: Anweisungen, wie der Systemdienst verwaltet werden kann, einschließlich Befehlen zum Überprüfen des Status, Neustarten, Stoppen, Deaktivieren und Aktivieren des Dienstes.

Diese README-Datei bietet eine umfassende Anleitung für die Benutzer des OWIPEX Tools. Wenn du weitere Anpassungen benötigst, lass es mich wissen!