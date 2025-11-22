# Pemrograman Jaringan – Tiga Program TCP (Python)

Repository ini berisi tiga implementasi program TCP Socket dalam bahasa **Python**, sesuai tugas mata kuliah *Pemrograman Jaringan*.  
Setiap soal dipisahkan dalam branch berbeda untuk menjaga struktur dan kerapian kode.

---

## Struktur Branch

| Branch | Deskripsi |
|--------|-----------|
| `main` | Hanya berisi README.md |
| `TCP-Echo-Server` | Implementasi TCP Echo Server & Client |
| `Multithreaded-TCP-Chat-Server` | Multithreaded TCP Chat Server dengan broadcast |
| `Implementasi-Timeout` | TCP Client dengan timeout connect & read |

---

# **TCP Echo Server**
Program dasar yang terdiri dari server TCP pada port **5050** dan client sederhana.  
Server menerima pesan dari client, menampilkannya, lalu mengembalikan pesan tersebut (echo).  
Client menampilkan balasan dari server.

---

# **Multithreaded TCP Chat Server**
Server TCP yang mampu menangani banyak client secara paralel menggunakan multithreading.  
Setiap pesan yang diterima server akan dibroadcast ke seluruh client lain.  
Terdiri dari:  
- Server multithread  
- Client chat interaktif  
- Mendukung minimal 3 client terhubung sekaligus

---

# **TCP Client Timeout**
Implementasi client TCP dengan konfigurasi timeout
- Timeout **3 detik** saat melakukan koneksi  
- Timeout **2 detik** saat membaca data dari server 
