# Representasi Pohon Keluarga (Pohon 1)
pohon_keluarga = {
    "Hadi_Retno": {  # Kakek dan Nenek
        "anak": {
            "Bayu": ["Fahrul", "Tari"], 
            "Desi": ["Nurul", "Aji"], 
            "Wahyu": ["Yanto", "Gunawan"], 
            "Rina": ["Hamzah"], 
            "Ardi": ["Eka", "Mira", "Bastian"]
        },
        "cucu": {
            "Fahrul": ["Wanda"],
            "Nurul": ["Aji"],
            "Yanto": ["Gunawan"],
            "Mira": ["Anggun", "Boy"]
        }
    }
}

# Relasi Keluarga
relasi = {
    "orang_tua": ["Hadi", "Retno"],
    "anak": ["Bayu", "Desi", "Wahyu", "Rina", "Ardi"],
    "cucu": ["Fahrul", "Tari", "Nurul", "Yanto", "Hamzah", "Eka", "Mira", "Bastian"],
    "kakek_nenek": ["Hadi", "Retno"],
    "sepupu": {
        "Fahrul": ["Nurul", "Yanto", "Hamzah", "Eka", "Mira", "Bastian"],
        "Nurul": ["Fahrul", "Yanto", "Hamzah", "Eka", "Mira", "Bastian"],
        # Tambahkan relasi sepupu lain
    }
}

# Fungsi untuk Menampilkan Relasi Keluarga
def tampilkan_relasi():
    print("=== Representasi Pengetahuan Pohon Keluarga ===")
    for kakek_nenek, detail in pohon_keluarga.items():
        print(f"Kakek & Nenek: {kakek_nenek.replace('_', ' dan ')}")
        print("  Anak-anak:")
        for anak, cucu in detail["anak"].items():
            print(f"    - {anak}: {', '.join(cucu)}")
        print("  Cucu:")
        for cucu, cicit in detail["cucu"].items():
            print(f"    - {cucu}: {', '.join(cicit)}")

# Fungsi untuk Mengubah Nama Berdasarkan Instruksi
def ubah_nama(nim, nama):
    digit_ke_8 = int(nim[7])  # Index Python dimulai dari 0
    digit_ke_7 = int(nim[6])

    nama_parts = nama.split()
    if len(nama_parts) < 3:
        print("Nama harus terdiri dari setidaknya 3 bagian (depan, tengah, belakang).")
        return nama

    # Ubah nama depan (digit ke-8)
    if 0 <= digit_ke_8 <= 9:
        nama_parts[0] = nama_parts[1]  # Nama depan diganti dengan nama tengah

    # Ubah nama tengah (digit ke-7)
    if 0 <= digit_ke_7 <= 9:
        nama_parts[1] = nama_parts[2]  # Nama tengah diganti dengan nama belakang

    return " ".join(nama_parts)

# Contoh Penggunaan
nim_mahasiswa = "23422060"
nama_mahasiswa = "Daniel Achmad Farizki"
nama_baru = ubah_nama(nim_mahasiswa, nama_mahasiswa)

print("Nama asli:", nama_mahasiswa)
print("Nama setelah diubah:", nama_baru)

# Tampilkan Relasi Keluarga
tampilkan_relasi()
