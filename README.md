# NISG2024 Checker

Dieses Projekt überprüft, ob Ihr Unternehmen von der NIS2-Richtlinie betroffen ist und zeigt die entsprechenden Pflichten und Risikomanagementmaßnahmen.

## Disclaimer

Bitte beachten Sie, dass diese Information keine Rechtsberatung zur NIS2 darstellt. Für rechtliche Beratung wenden Sie sich bitte an Ihren Rechtsberater oder Ihre Wirtschaftsvertretung, beispielsweise die WKÖ.

## Anforderungen

- Docker
- Python 3.9 oder höher (für die Python-Variante)

## Installation und Ausführung

### Variante 1: Mit Docker

#### Schritt 1: Klonen Sie das Repository

Zuerst müssen Sie das Repository auf Ihren lokalen Rechner klonen. Öffnen Sie dazu ein Terminal und führen Sie den folgenden Befehl aus:

```sh
git clone https://github.com/yourusername/nisg2024_checker.git
cd nisg2024_checker
```

#### Schritt 2: Erstellen Sie das Docker-Image

Erstellen Sie nun das Docker-Image, indem Sie den folgenden Befehl im Terminal ausführen:

```sh
docker build -t nisg2024_checker .
```

Dieser Befehl erstellt ein Docker-Image mit dem Namen `nisg2024_checker` basierend auf dem im `Dockerfile` definierten Build-Prozess.

#### Schritt 3: Starten Sie den Docker-Container

Nachdem das Docker-Image erfolgreich erstellt wurde, können Sie den Docker-Container starten:

```sh
docker run -it nisg2024_checker
```

Der obige Befehl startet einen interaktiven Docker-Container und führt das Programm aus.

### Variante 2: Mit Python

#### Schritt 1: Klonen Sie das Repository

Klonen Sie das Repository auf Ihren lokalen Rechner, falls noch nicht geschehen:

```sh
git clone https://github.com/yourusername/nisg2024_checker.git
cd nisg2024_checker/app
```

#### Schritt 2: Erstellen Sie eine virtuelle Umgebung

Um eine isolierte Python-Umgebung zu erstellen, führen Sie die folgenden Befehle aus:

```sh
python -m venv env
source env/bin/activate  # Auf Windows verwenden Sie `env\Scripts\activate`
```

Die virtuelle Umgebung stellt sicher, dass die Abhängigkeiten des Projekts nicht mit anderen Python-Projekten auf Ihrem Rechner kollidieren.

#### Schritt 3: Installieren Sie die Abhängigkeiten

Installieren Sie die erforderlichen Python-Pakete mit `pip`:

```sh
pip install -r requirements.txt
```

#### Schritt 4: Starten Sie das Programm

Führen Sie das Programm aus, indem Sie den folgenden Befehl im Terminal eingeben:

```sh
python main.py
```

## Benutzung

Nach dem Start des Programms werden Sie durch eine Reihe von Eingabeaufforderungen geführt, um verschiedene Informationen über Ihr Unternehmen einzugeben. Diese Informationen werden verwendet, um festzustellen, ob Ihr Unternehmen von der NIS2-Richtlinie betroffen ist.

### Eingabeaufforderungen

1. **Wählen Sie einen Sektor:** Sie werden aufgefordert, einen Sektor aus einer Liste auszuwählen. Geben Sie die entsprechende Nummer des Sektors ein.
2. **Name des Unternehmens:** Geben Sie den Namen Ihres Unternehmens ein.
3. **Anzahl der Mitarbeiter:** Geben Sie die Anzahl der Mitarbeiter in Ihrem Unternehmen ein.
4. **Jahresumsatz in Millionen Euro:** Geben Sie den Jahresumsatz Ihres Unternehmens in Millionen Euro ein.

### Ausgabe

Basierend auf Ihren Eingaben wird das Programm Folgendes anzeigen:

- **Unternehmensname**
- **Sektor**
- **Unternehmensgröße** (kleines, mittleres oder großes Unternehmen)
- **Einrichtungsart** (wesentliche Einrichtung, wichtige Einrichtung oder nicht betroffen)

Wenn Ihr Unternehmen als wesentliche oder wichtige Einrichtung eingestuft wird, zeigt das Programm die entsprechenden Pflichten und Risikomanagementmaßnahmen an, die gemäß der NIS2-Richtlinie erforderlich sind.

### Beispielausgabe

```
*** NISG2024 (Entwurf) Checker ***
Dieses Programm überprüft, ob Ihr Unternehmen von der NIS2-Richtlinie betroffen ist
und zeigt die entsprechenden Pflichten und Risikomanagementmaßnahmen

Bitte wählen Sie einen Sektor aus der folgenden Liste aus:
1. Energie
2. Verkehr
3. Bankwesen
4. Finanzmarktinfrastrukturen
5. Gesundheitswesen
6. Trinkwasser
7. Abwasser
8. Verwaltung von IKT-Diensten B2B
9. öffentliche Verwaltung
10. Weltraum
11. Digitale Infrastruktur
12. Post- und Kurierdienste
13. Abfallbewirtschaftung
14. Chemie
15. Lebensmittel
16. Verarbeitendes/herstellendes Gewerbe
17. Anbieter digitaler Dienste
18. Forschung

Geben Sie die Nummer des gewählten Sektors ein: 1
Name des Unternehmens: Beispiel GmbH
Anzahl der Mitarbeiter: 200
Jahresumsatz in Millionen Euro: 30

---------------------------------------
            Ergebnisse
---------------------------------------
Unternehmen: Beispiel GmbH
Sektor: Energie
Unternehmensgröße: Mittleres Unternehmen
Einrichtungsart: Wesentliche Einrichtung

Pflichten für wesentliche und wichtige Einrichtungen:
§29 Registrierungspflicht
§31 Verantwortung der Leitungsorgane für die Einhaltung der Risikomanagementmaßnahmen
    Teilnahme an Cybersicherheitsschulungen
§32 Implementierung technischer, operativer und organisatorischer Maßnahmen zur Beherrschung der Risiken
§33 Nachweis über die Wirksamkeit der Risikomaßnahmen
§34 Verpflichtung zur Meldung erheblicher Cybersicherheitsvorfälle und regelmäßige Berichterstattung über die umgesetzten Sicherheitsmaßnahmen
§35 Beurteilung erheblicher Cybersicherheitsvorfall
§42 Definition der Arten personenbezogener Daten, die bei Sicherheitsvorfällen gemeldet werden müssen

Erfüllung von 10 Risikomanagementmaßnahmen gemäß Artikel 21 der NIS2-Richtlinie:
1. Risikoanalyse und Sicherheitskonzepte für Informationssysteme
2. Bewältigung von Sicherheitsvorfällen
3. Aufrechterhaltung des Betriebs (Backup-Management und Wiederherstellung nach einem Notfall, Krisenmanagement)
4. Sicherheit der Lieferkette
5. Sicherheitsmaßnahmen bei Erwerb, Entwicklung und Wartung von Netz- und Informationssystemen
6. Bewertung der Wirksamkeit von Risikomanagementmaßnahmen
7. Cyberhygiene und Schulungen im Bereich Cybersicherheit
8. Einsatz von Kryptografie und Verschlüsselung
9. Sicherheit des Personals, Zugriffskontrollen, Management von Anlagen
10. Multi-Faktor-Authentifizierung und gesicherte Kommunikation

Weitere Informationen finden Sie im Anhang 3 zu NISG 2024 Entwurf

Ihr Unternehmen ist nicht von der NIS2-Richtlinie betroffen.
```

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der `LICENSE`-Datei.
```

Dieses ausführliche `README.md`-Dokument bietet eine umfassende Anleitung zur Installation und Ausführung des Programms, sowohl mit Docker als auch mit Python, sowie detaillierte Informationen zur Nutzung des Programms.
