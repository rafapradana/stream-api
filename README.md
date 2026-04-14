# Stream API

Real-time data streaming API menggunakan Flask dan Server-Sent Events (SSE) dengan PostgreSQL sebagai database.

## Prerequisites

- Python 3.8+
- PostgreSQL
- pip

## Instalasi

1. Clone repository:

```bash
git clone https://github.com/rafapradana/stream-api.git
cd stream-api
```

2. Buat virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Setup Database

1. Pastikan PostgreSQL sudah berjalan

2. Buat database bernama `stream`:

```sql
CREATE DATABASE stream;
```

3. Jalankan migrasi schema:

```bash
psql -U postgres -d stream -f db.sql
```

**Konfigurasi default:**
- Host: `localhost`
- Database: `stream`
- User: `postgres`
- Password: `postgres`

Jika ingin mengubah konfigurasi, edit file `api.py` dan `generate.py` pada bagian koneksi database.

## Generate Data

Generate 10.000 data dummy ke database:

```bash
python generate.py
```

## Menjalankan Aplikasi

```bash
python api.py
```

Aplikasi akan berjalan di `http://localhost:5000`

## Fitur

- **Real-time Streaming**: Data di-stream menggunakan Server-Sent Events (SSE)
- **Dark/Light Theme**: Toggle tema dengan tombol atau simpan preferensi di localStorage
- **Search**: Filter data secara real-time (tekan `F` untuk fokus)
- **Pause/Resume**: Pause dan resume stream (tekan `Space`)
- **Auto-scroll**: Otomatis scroll ke data terbaru
- **Export CSV**: Download data yang sudah diterima dalam format CSV
- **Detail Panel**: Klik baris untuk melihat detail data
- **Keyboard Shortcuts**:
  - `Space` - Pause/Resume stream
  - `F` - Fokus ke search
  - `R` - Reconnect stream
  - `D` - Toggle detail panel

## Struktur Project

```
stream-api/
├── api.py           # Flask API dengan SSE endpoint
├── generate.py      # Script generate data dummy
├── page.html        # Frontend viewer
├── db.sql           # Schema database
├── requirements.txt # Dependencies Python
└── .gitignore       # Git ignore file
```

## API Endpoints

| Endpoint   | Method | Description                    |
|------------|--------|--------------------------------|
| `/`        | GET    | Halaman viewer SSE             |
| `/stream`  | GET    | SSE stream data dari database  |
