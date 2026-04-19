---
title: Atomic Presence Support
layout: simple
summary: Support and contact for Atomic Presence
app_slug: atomic-presence
showDate: false
showReadingTime: false
---

[App Store](https://apps.apple.com/app/id6759192866) · [Privacy Policy](/en/privacy/atomic-presence/)

---

## FAQ

**Q: The QR code is unclear in the video and can't be scanned during verification?**  
A: Ensure sufficient screen brightness during recording, and keep the camera 30–50 cm from the screen. The QR code updates once per second — the camera needs to be able to focus clearly. If the problem persists, try reducing the recording resolution.

**Q: Audio watermark verification fails?**  
A: Watermark verification may fail if: the audio was heavily compressed (e.g., forwarded via WhatsApp), the audio was truncated, or there was excessive background noise. Record in a quiet environment and use the original audio file for verification.

**Q: The digital signature is invalid on a new device?**  
A: Each device's signing key is stored in the iOS Keychain, and a new device generates a different key. You do NOT need to manually export the public key — every `.evidence.json` written by the app already embeds the public key used for that recording's signature, so any verifier who holds the evidence file can verify it regardless of which device they're on.

**Q: The app crashed during recording — is the file still there?**  
A: When the app crashes unexpectedly, partial recordings may remain in the Documents directory. Reopen the app, tap the **VERIFY** button at the top of the main screen, and check the three tabs (Level 1 / Level 2 / Level 3) for any recoverable files.

**Q: Hash chain verification shows "integrity broken" but I didn't edit the recording?**  
A: Possible causes include: the app was interrupted by the system during recording, low battery, or a write error due to insufficient storage. Ensure sufficient battery and storage before recording.

---

## Troubleshooting

1. **Ensure the device has sufficient storage** (recommend at least 2 GB available)
2. **Keep the screen on during recording** to avoid system interruptions
3. **Force quit and relaunch the app**
4. **Check iOS version** ≥ 17.0
5. If a specific scenario consistently causes issues, screenshot the error message and email us

---

## Contact Support

📧 **qqder339@gmail.com**  
Subject: `[Atomic Presence] Issue Description`

Please include: device model, iOS version, app version, recording mode (video/audio), steps to reproduce.

> This app collects no user data. All cryptographic operations run entirely on-device. We have no access to your recordings. [View Privacy Policy →](/en/privacy/atomic-presence/)
