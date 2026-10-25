# PBL0302 - Car Data CRUDS (Django)

Aplikasi web sederhana untuk mengelola data mobil (**Create, Read, Update, Delete, Search**) menggunakan framework **Django** dan database **SQLite**.

## Informasi

- Nama: MUCHAMAD FARID FIRDAUS
- NIM: 251080200089
- Tugas: PBL0302
- Framework: Python - Django
- Database: SQLite (`carsweb.db`)

## Fitur

| Fitur | Keterangan |
|---|---|
| Create | Menambah data mobil baru |
| Read | Menampilkan seluruh data mobil dalam tabel |
| Update | Mengubah data mobil yang sudah ada |
| Delete | Menghapus data mobil (dengan halaman konfirmasi) |
| Search | Mencari berdasarkan nama, brand, atau model |

## Sumber Data

Data memakai `carsweb.db` dari repositori dosen
([hepidad/c003-monolith](https://github.com/hepidad/c003-monolith)).
Tabel `tbcars` berisi kolom `carname`, `carbrand`, `carmodel`, dan `carprice`.
Model Django dipetakan ke tabel tersebut dengan `managed = False`,
sehingga Django tidak mengubah struktur tabelnya.

## Struktur Proyek

```
PBL0302_CARS/
├── manage.py
├── carsweb.db
├── carsproject/        # pengaturan proyek (settings, urls)
└── cars/               # aplikasi utama
    ├── models.py       # model Car (tabel tbcars)
    ├── forms.py        # form Create dan Update
    ├── views.py        # logika CRUDS
    ├── urls.py         # routing aplikasi
    └── templates/cars/ # tampilan HTML
```

## Cara Menjalankan

1. Clone repositori:

```
git clone https://github.com/faridfirdaus244-gif/pbl0302-cars-django.git
cd pbl0302-cars-django
```

2. Buat dan aktifkan virtual environment (Windows PowerShell):

```
python -m venv env
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\env\Scripts\Activate.ps1
```

3. Install Django:

```
pip install django
```

4. Jalankan server:

```
python manage.py runserver
```

5. Buka http://127.0.0.1:8000 di browser.

Catatan: jangan menjalankan `python manage.py migrate`, karena perintah itu
menambahkan tabel bawaan Django ke dalam `carsweb.db`. Peringatan
"unapplied migrations" saat server berjalan dapat diabaikan.