---
title: Dukungan Atomic Presence
layout: simple
summary: Support and contact for Atomic Presence
app_slug: atomic-presence
showDate: false
showReadingTime: false
---

[App Store](https://apps.apple.com/app/id6759192866) · [Kebijakan Privasi](/en/privacy/atomic-presence/)

---

## Pertanyaan Umum

**T: QR code di video tidak jelas dan tidak bisa dipindai saat verifikasi?**  
J: Pastikan kecerahan layar cukup saat perekaman, dan jaga jarak kamera 30–50 cm dari layar. QR code diperbarui sekali per detik — kamera harus bisa fokus dengan jelas. Jika masalah berlanjut, coba turunkan resolusi perekaman.

**T: Verifikasi watermark audio gagal?**  
J: Verifikasi watermark dapat gagal jika: audio dikompresi berat (misalnya diteruskan lewat WhatsApp), audio terpotong, atau terdapat kebisingan latar yang berlebihan. Rekam di lingkungan yang tenang dan gunakan file audio asli untuk verifikasi.

**T: Tanda tangan digital tidak valid di perangkat baru?**  
J: Kunci penandatanganan tiap perangkat disimpan di iOS Keychain, dan perangkat baru akan membuat kunci yang berbeda. Anda TIDAK perlu mengekspor kunci publik secara manual — setiap `.evidence.json` yang ditulis aplikasi sudah menyematkan kunci publik yang digunakan untuk tanda tangan rekaman tersebut, sehingga verifier mana pun yang memegang file bukti dapat memverifikasi tanpa tergantung perangkat.

**T: Aplikasi crash saat merekam — apakah filenya masih ada?**  
J: Saat aplikasi crash secara tak terduga, rekaman parsial bisa tetap tersimpan di direktori Documents. Buka ulang aplikasi, ketuk tombol **VERIFY** di bagian atas layar utama, lalu periksa tiga tab (Level 1 / Level 2 / Level 3) untuk file yang bisa dipulihkan.

**T: Verifikasi hash chain menampilkan "integrity broken" padahal saya tidak mengedit rekaman?**  
J: Kemungkinan penyebab: aplikasi sempat diinterupsi sistem saat merekam, baterai lemah, atau terjadi error tulis karena ruang penyimpanan tidak cukup. Pastikan baterai dan penyimpanan memadai sebelum merekam.

---

## Pemecahan masalah

1. **Pastikan perangkat memiliki penyimpanan yang cukup** (disarankan minimal 2 GB tersedia)
2. **Jaga layar tetap menyala saat perekaman** untuk menghindari interupsi sistem
3. **Paksa tutup lalu buka kembali aplikasi**
4. **Periksa versi iOS** ≥ 17.0
5. Jika skenario tertentu konsisten memicu masalah, ambil tangkapan layar pesan error dan kirim email kepada kami

---

## Hubungi dukungan

📧 **qqder339@gmail.com**  
Subjek: `[Atomic Presence] Issue Description`

Mohon sertakan: model perangkat, versi iOS, versi aplikasi, mode perekaman (video/audio), langkah reproduksi.

> Aplikasi ini tidak mengumpulkan data pengguna. Semua operasi kriptografis berjalan sepenuhnya di perangkat. Kami tidak memiliki akses ke rekaman Anda. [Lihat Kebijakan Privasi →](/en/privacy/atomic-presence/)
