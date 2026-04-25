---
title: Atomic Presence — Datenschutzrichtlinie
layout: simple
showDate: false
showReadingTime: false
---

**Zuletzt aktualisiert: 2026-04-15**

---

## 1. Überblick

Atomic Presence, entwickelt von QQder339, ist ein Anti-Deepfake-Tool, das kryptografische Hash chains, digitale Signaturen und Audio-Watermarking nutzt, damit Nutzer:innen die Integrität ihrer Aufnahmen selbst verifizieren können.

**Kurz gesagt: Wir erfassen, speichern oder übertragen KEINE Ihrer personenbezogenen Daten an externe Server. Alle kryptografischen Operationen und Verifizierungen erfolgen auf dem Gerät.**

## 2. Daten, die wir NICHT erfassen

Diese App erfasst nicht:

- Personenbezogene Daten (Name, E-Mail, Telefonnummer)
- Standortdaten
- Gerätekennungen
- Nutzungsanalysen oder Tracking-Daten

## 3. Lokal gespeicherte Daten

Die folgenden Daten werden ausschließlich auf Ihrem Gerät gespeichert und niemals extern übertragen:

- **Audio-/Videodateien**: Alle aufgenommenen Inhalte werden im lokalen Speicher Ihres Geräts abgelegt
- **Hash chain-Protokolle**: SHA-256-Hash-Sequenzen und zugehörige Verifizierungsdaten
- **Digitale Signaturen**: Signaturdaten, die per Curve25519-Algorithmus auf dem Gerät erzeugt werden
- **Verifizierungsberichte**: Integritätsberichte und Metadatenprotokolle
- **Anonymisierte Gerätekennung**: Jede `.evidence.json` enthält ein 16-stelliges Hex-Präfix von `SHA-256(identifierForVendor)`, das ausschließlich dazu dient, Aufnahmen desselben Geräts bei der Verifizierung zu korrelieren. Diese Kennung existiert nur in Evidenzdateien auf Ihrem Gerät, wird niemals an einen Server übertragen und kann nicht auf die ursprünglichen Geräteinformationen zurückgerechnet werden

## 4. Kryptografische Funktionen (vollständig offline)

Alle Kernfunktionen werden ohne Netzwerkverbindung auf dem Gerät ausgeführt:

- **Hash chain-Erzeugung**: Echtzeit-SHA-256-Hash-Sequenzen; sämtliche Berechnungen laufen lokal
- **Digitales Signieren**: Verwendet den Curve25519-Algorithmus zum Signieren von Aufnahmen auf dem Gerät
- **Audio-Watermarking**: Bettet FSK-Signale in Aufnahmen ein; die gesamte Signalverarbeitung läuft auf dem Gerät
- **Verifizierung**: Integritätsprüfung wird lokal berechnet

## 5. Wichtiger Hinweis

Die von dieser App verarbeiteten Inhalte (Audio, Video) können sensible Informationen enthalten. Die gesamte Verarbeitung erfolgt auf Ihrem Gerät, und **wir können und werden niemals auf Ihre aufgenommenen Inhalte zugreifen**.

## 6. Dienste von Drittanbietern

Diese App verwendet **KEINE** Analyse- oder Werbe-Frameworks von Drittanbietern (No Google Analytics, No Facebook SDK, No Ads).

## 7. Netzwerkzugriff

Diese App benötigt **keine Netzwerkverbindung**, um alle Funktionen zu nutzen. Der einzige Netzwerkzugriff ist:

- **Externe Links**: Öffnet den Browser beim Antippen relevanter Links

## 8. Kontakt

📧 **qqder339@gmail.com**  
Betreff: Anfrage zur Atomic Presence Datenschutzrichtlinie
