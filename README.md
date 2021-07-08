# SEGA (Sequence Diagram Generation) 1.0
> Generate dari Use Case Specification ke Sequence Diagram dengan Model Robustness

Proyek ini merupakan proyek untuk menghasilkan artefak UML berupa diagram sequence dengan model robustness dari spesifikasi use case. Proyek ini dikembangkan oleh kelompok 1 (kelas I2) pada mata kuliah Pembangunan Perangkat Lunak S1 Sistem Informasi UNAIR.

# Daftar Isi
* [Deskripsi Proyek](#deskripsi-proyek)
  * [Tentang Proyek](#tentang-proyek)
  * [Fitur](#fitur)
* [Petunjuk Instalasi](#petunjuk-instalasi)
* [Langkah-Langkah Penggunaan](#langkah-langkah-penggunaan)
* [Informasi Lainnya](#informasi-lainnya)
  * [Anggota Proyek](#anggota-proyek)
  * [Link](#link)
  * [Kontak](#kontak)
* [Lisensi](#lisensi)

# Deskripsi Proyek
### Tentang Proyek
SEGA (Sequence Diagram Generation) merupakan proyek Django berbasis website yang melibatkan artefak spesifikasi use case dan diagram sequence. Tujuan pembuatan SEGA adalah untuk mewujudkan translasi dari spesifikasi use case menjadi diagram sequence dalam output berupa script PlantUML. Proses translasi yang terdapat dalam proyek SEGA dilakukan dengan memanfaatkan spesifikasi use case untuk mendapatkan diagram sequence. Form input dimanfaatkan untuk memasukkan detail spesifikasi use case, berupa aktor, nama use case, objek, skenario normal, dan skenario alternatif.

### Fitur
1. Generate diagram sequence dengan model robustness dari spesifikasi use case secara otomatis.
2. Form untuk input spesifikasi use case.
3. Hasil generate dalam bentuk UMLscript yang dapat digunakan di PlantUML.

# Petunjuk Instalasi
1. Lakukan instalasi dan setup Django terlebih dahulu. [Petunjuk instalasi dan setup Django](https://docs.djangoproject.com/en/3.2/intro/install/)
2. Download atau clone proyek, lalu simpan di dalam folder untuk proyek Django.
   ```sh
   git clone https://github.com/AgileRE-2021/UseCaseSpecToSequence.git
   ```
3. Pindah ke folder proyek.
   ```sh
   cd .../<folder Django>/<folder proyek>
   ```
4. Jalankan perintah-perintah di bawah ini.
   ```sh
   git fetch --all
   ```
   ```sh
   git checkout -b backend-usecase
   ```
   ```sh
   git pull
   ```
5. Jalankan server.
   ```sh
   python manage.py runserver
   ```
6. Buka browser, lalu masukkan alamat
   ```sh
   https://localhost:8000/generation
   ```
   atau
   ```sh
   https://localhost:8000/generation/home
   ```

# Langkah-Langkah Penggunaan
1. Jalankan server terlebih dahulu.
2. Klik tombol Add Project, lalu isi form-nya untuk membuat project.
3. Setelah dibuat, klik View project untuk memasuki halaman list use case.
4. Klik tombol Add Usecase, lalu isi nama use case-nya.
5. Setelah dibuat, klik View use case memasuki halaman form spesifikasi use case.
6. Isi bagian-bagian sebelum skenario (Actor, Use Case Name, Description, Pre-condition, Pre-condition object, Post-condition, dan Post-condition object) terlebih dahulu, lalu klik tombol Submit.
7. Isi langkah-langkah pada skenario normal dan alternatif (jika ada), lalu klik tombol Save.
8. Setelah di-save, klik tombol Generate Diagram untuk menghasilkan UMLscript-nya.
9. Copy hasilnya, lalu buka [PlantUML](https://plantuml.com/plantuml) dan paste hasilnya.
10. Klik tombol Submit untuk menghasilkan diagram sequence-nya.

# Informasi Lainnya
### Anggota Kelompok 1 (kelas I2)
1. Naufal Ghani Achmani (081811633001)
2. Fahmirullah Abdillah (081811633002)
3. Muhammad Faris Arifin (081811633006)
4. Rr Arnetta Dinda Yuanita (081811633009)
5. Alexander Ryan Hendarto (081811633010)
6. Twenty Oktavia Pujiliana (081811633024)
7. Dean Farrel Radiany Wibowo (081811633054)

### Link
* Dokumentasi proyek
* Dataset

### Kontak
1. Naufal Ghani Achmani: naufalghaniachmani@gmail.com
2. Fahmirullah Abdillah: fahmirull17@gmail.com
3. Muhammad Faris Arifin: farisarifin99@gmail.com
4. Rr Arnetta Dinda Yuanita: arnettadindayuanita@gmail.com
5. Alexander Ryan Hendarto: alexanderryan38@gmail.com
6. Twenty Oktavia Pujiliana: stefani.via.sv@gmail.com
7. Dean Farrel Radiany Wibowo: stigma0602@gmail.com

# Lisensi
Copyright © 2021 S1 Sistem Informasi Universitas Airlangga
