---
title: Atomic Presence Support
layout: simple
summary: Support and contact for Atomic Presence
app_slug: atomic-presence
showDate: false
showReadingTime: false
---

[App Store](https://apps.apple.com/app/id6759192866) · [Datenschutzrichtlinie](/en/privacy/atomic-presence/)

---

## Häufige Fragen

**F: Der QR code ist im Video unscharf und kann bei der Verifizierung nicht gescannt werden?**  
A: Stellen Sie während der Aufnahme eine ausreichende Bildschirmhelligkeit sicher und halten Sie die Kamera 30–50 cm vom Bildschirm entfernt. Der QR code wird einmal pro Sekunde aktualisiert — die Kamera muss sauber fokussieren können. Wenn das Problem bleibt, versuchen Sie, die Aufnahmeauflösung zu reduzieren.

**F: Die Audio-Watermark-Verifizierung schlägt fehl?**  
A: Die Watermark-Verifizierung kann fehlschlagen, wenn: das Audio stark komprimiert wurde (z. B. über WhatsApp weitergeleitet), das Audio gekürzt wurde oder starke Hintergrundgeräusche vorhanden waren. Nehmen Sie in ruhiger Umgebung auf und verwenden Sie zur Verifizierung die originale Audiodatei.

**F: Die digitale Signatur ist auf einem neuen Gerät ungültig?**  
A: Der Signaturschlüssel jedes Geräts wird im iOS Keychain gespeichert, und ein neues Gerät erzeugt einen anderen Schlüssel. Sie müssen den öffentlichen Schlüssel NICHT manuell exportieren — jede von der App geschriebene `.evidence.json` enthält bereits den öffentlichen Schlüssel, der für diese Aufnahme-Signatur verwendet wurde. Dadurch kann jede prüfende Person mit der Evidenzdatei verifizieren, unabhängig vom verwendeten Gerät.

**F: Die App ist während der Aufnahme abgestürzt — ist die Datei noch vorhanden?**  
A: Wenn die App unerwartet abstürzt, können Teilaufnahmen im Documents-Verzeichnis verbleiben. Öffnen Sie die App erneut, tippen Sie oben im Hauptbildschirm auf **VERIFY** und prüfen Sie die drei Tabs (Stufe 1 / Stufe 2 / Stufe 3) auf wiederherstellbare Dateien.

**F: Bei der Hash chain-Verifizierung steht "integrity broken", aber ich habe die Aufnahme nicht bearbeitet?**  
A: Mögliche Ursachen sind: Die App wurde während der Aufnahme vom System unterbrochen, niedriger Akkustand oder ein Schreibfehler wegen zu wenig Speicherplatz. Stellen Sie vor der Aufnahme ausreichend Akku und Speicher sicher.

---

## Fehlerbehebung

1. **Sicherstellen, dass das Gerät genügend Speicher hat** (mindestens 2 GB empfohlen)
2. **Bildschirm während der Aufnahme eingeschaltet lassen**, um Systemunterbrechungen zu vermeiden
3. **App zwangsbeenden und neu starten**
4. **iOS-Version prüfen** ≥ 17.0
5. Wenn ein bestimmtes Szenario reproduzierbar Probleme verursacht, machen Sie einen Screenshot der Fehlermeldung und senden Sie uns eine E-Mail

---

## Support kontaktieren

📧 **qqder339@gmail.com**  
Betreff: `[Atomic Presence] Issue Description`

Bitte angeben: Gerätemodell, iOS-Version, App-Version, Aufnahmemodus (Video/Audio), Reproduktionsschritte.

> Diese App erfasst keine Nutzerdaten. Alle kryptografischen Operationen laufen vollständig auf dem Gerät. Wir haben keinen Zugriff auf Ihre Aufnahmen. [Datenschutzrichtlinie anzeigen →](/en/privacy/atomic-presence/)
