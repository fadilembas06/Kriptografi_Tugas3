import hashlib
import json

def buat_md5(data: dict) -> str:
    """Membuat hash MD5 dari dictionary data profil."""
    data_str = json.dumps(data, sort_keys=True)
    return hashlib.md5(data_str.encode()).hexdigest()

def input_data_profil(label: str) -> dict:
    """Menerima input data profil dari user."""
    print(f"\n{'─'*40}")
    print(f"  Masukkan {label}:")
    print(f"{'─'*40}")
    nama     = input("  Nama      : ").strip()
    email    = input("  Email     : ").strip()
    nomor_hp = input("  Nomor HP  : ").strip()
    return {"nama": nama, "email": email, "nomor_hp": nomor_hp}

def tampilkan_perbandingan(hash_lama: str, hash_baru: str):
    """Menampilkan hash lama, hash baru, dan status perubahan."""
    print(f"\n{'='*55}")
    print("  HASIL PERBANDINGAN HASH MD5")
    print(f"{'='*55}")
    print(f"  Hash Lama  : {hash_lama}")
    print(f"  Hash Baru  : {hash_baru}")
    print(f"{'─'*55}")

    if hash_lama == hash_baru:
        print("  Status     : ✅ DATA TIDAK BERUBAH")
        print("               Profil user masih sama seperti sebelumnya.")
    else:
        print("  Status     : ⚠️  DATA TELAH DIMODIFIKASI!")
        print("               Profil user mengalami perubahan.")
    print(f"{'='*55}")

# ──────────────────────────────────────────────
#  PROGRAM UTAMA
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("╔═════════════════════════════════════════════════════╗")
    print("║    Sistem Deteksi Perubahan Profil User (MD5)       ║")
    print("╚═════════════════════════════════════════════════════╝")

    # LANGKAH 1 — Terima input data awal user
    print("\n📥 LANGKAH 1: Input Data Profil Awal")
    data_awal = input_data_profil("Data Profil Awal")

    # LANGKAH 2 — Buat hash MD5 dari data awal
    hash_awal = buat_md5(data_awal)
    print(f"\n🔐 Hash MD5 awal disimpan : {hash_awal}")

    # LANGKAH 3 — Terima input data baru (setelah kemungkinan perubahan)
    print("\n📥 LANGKAH 2: Input Data Profil Baru (untuk dibandingkan)")
    data_baru = input_data_profil("Data Profil Baru")

    # LANGKAH 4 — Buat hash MD5 dari data baru
    hash_baru = buat_md5(data_baru)

    # LANGKAH 5 — Bandingkan dan tampilkan hasil
    tampilkan_perbandingan(hash_awal, hash_baru)