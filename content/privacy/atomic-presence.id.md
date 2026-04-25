---
title: Atomic Presence — Kebijakan Privasi
layout: simple
showDate: false
showReadingTime: false
---

**Terakhir diperbarui: 2026-04-15**

---

## 1. Ikhtisar

Atomic Presence, dikembangkan oleh QQder339, adalah alat anti-deepfake yang menggunakan hash chain kriptografis, tanda tangan digital, dan watermarking audio untuk membantu pengguna memverifikasi sendiri integritas rekaman mereka.

**Singkatnya: Kami TIDAK mengumpulkan, menyimpan, atau mengirimkan data pribadi Anda ke server eksternal. Semua operasi kriptografis dan verifikasi dilakukan di perangkat.**

## 2. Data yang TIDAK kami kumpulkan

Aplikasi ini tidak mengumpulkan:

- Informasi identitas pribadi (nama, email, nomor telepon)
- Data lokasi
- Pengenal perangkat
- Data analitik penggunaan atau pelacakan

## 3. Data yang disimpan secara lokal

Data berikut disimpan sepenuhnya di perangkat Anda dan tidak pernah ditransmisikan ke luar:

- **File Audio/Video**: semua konten rekaman disimpan di penyimpanan lokal perangkat Anda
- **Catatan Hash chain**: urutan hash SHA-256 dan data verifikasi terkait
- **Tanda Tangan Digital**: data tanda tangan yang dihasilkan algoritma Curve25519 di perangkat
- **Laporan Verifikasi**: laporan integritas dan catatan metadata
- **Pengenal perangkat anonim**: setiap `.evidence.json` menyematkan prefiks heksadesimal 16 karakter dari `SHA-256(identifierForVendor)`, yang hanya digunakan untuk mengorelasikan rekaman dari perangkat yang sama saat verifikasi. Pengenal ini hanya berada di dalam file bukti pada perangkat Anda, tidak pernah dikirim ke server mana pun, dan tidak dapat dibalik ke informasi perangkat aslinya

## 4. Fitur kriptografis (sepenuhnya offline)

Semua fitur inti dijalankan di perangkat tanpa koneksi jaringan:

- **Pembuatan Hash chain**: urutan hash SHA-256 real-time; seluruh komputasi berjalan lokal
- **Penandatanganan Digital**: menggunakan algoritma Curve25519 untuk menandatangani rekaman di perangkat
- **Watermarking Audio**: menyematkan sinyal FSK ke rekaman; seluruh pemrosesan sinyal berjalan di perangkat
- **Verifikasi**: verifikasi integritas dihitung secara lokal

## 5. Catatan penting

Konten yang diproses aplikasi ini (audio, video) dapat berisi informasi sensitif. Seluruh pemrosesan terjadi di perangkat Anda, dan **kami tidak dapat dan tidak akan pernah mengakses konten rekaman Anda**.

## 6. Layanan pihak ketiga

Aplikasi ini **TIDAK** menggunakan framework analitik atau iklan pihak ketiga (No Google Analytics, No Facebook SDK, No Ads).

## 7. Akses jaringan

Aplikasi ini **tidak memerlukan koneksi jaringan** untuk menggunakan semua fitur. Satu-satunya akses jaringan adalah:

- **Tautan eksternal**: membuka browser saat mengetuk tautan terkait

## 8. Hubungi kami

📧 **qqder339@gmail.com**  
Subjek: Pertanyaan Kebijakan Privasi Atomic Presence
