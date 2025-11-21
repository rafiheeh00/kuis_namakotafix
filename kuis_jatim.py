#!/usr/bin/env python3
"""
Judul      : Kuis Tebak Nama Kota Jawa Timur
Versi      : 1.0
Deskripsi  : Program kuis berbasis teks mengenai tebak nama kota di Jawa Timur.
Penulis    : (Isi Nama Peserta)
"""

# ====== IMPORT DASAR ======
import sys
import re

# ====== METADATA ======
APP_NAME = "Kuis Tebak Nama Kota Jawa Timur"
APP_VERSION = "1.0"

# ====== DATA 10 SOAL ======
questions = [
    {"q": "Kota apa yang menjadi ibu kota Provinsi Jawa Timur?",
     "a": "surabaya"},

    {"q": "Kota mana yang dijuluki sebagai Kota Pendidikan di Jawa Timur?",
     "a": "malang"},

    {"q": "Kota mana yang dikenal sebagai pusat industri kereta api Indonesia?",
     "a": "madiun"},

    {"q": "Kota apa yang terkenal dengan ikon Simpang Lima Gumul?",
     "a": "kediri"},

    {"q": "Kota mana yang dikenal sebagai Kota Reog?",
     "a": "ponorogo"},

    {"q": "Kota apa yang menjadi pusat pemerintahan Kabupaten Banyuwangi?",
     "a": "banyuwangi"},

    {"q": "Kota mana yang dikenal sebagai Kota Santri di Jawa Timur?",
     "a": "jombang"},

    {"q": "Kota apa yang dikenal dengan industri marmernya?",
     "a": "tulungagung"},

    {"q": "Kota mana yang dikenal sebagai pintu menuju kawasan Gunung Bromo?",
     "a": "probolinggo"},

    {"q": "Kota apa yang dikenal dengan pelabuhan besar dan industri semen di Jawa Timur?",
     "a": "gresik"}
]


# ====== LOGIKA PEMERIKSAAN JAWABAN (VERSI PALING STABIL) ======

def is_correct(user_answer, correct_answer):
    ua = user_answer.strip().lower()
    ca = correct_answer.strip().lower()

    # 1. Jika kosong → salah
    if ua == "":
        return False

    # 2. Jika mengandung angka atau simbol → salah (madiun!!, kediri123, dll.)
    if re.search(r"[^a-zA-Z\s]", ua):
        return False

    # 3. Deteksi negasi → salah
    NEGATION = ["bukan", "tidak", "nggak", "gak", "bkn"]
    for neg in NEGATION:
        if ua.startswith(neg) or f" {neg} " in ua:
            return False

    # 4. Hapus "kota " hanya jika di depan (bukan di tengah)
    if ua.startswith("kota "):
        ua = ua[5:].strip()

    # 5. Normalisasi spasi
    ua = re.sub(r"\s+", " ", ua).strip()

    tokens = ua.split()
    if not tokens:
        return False

    # 6. Jawaban benar harus berada di kata terakhir
    if tokens[-1] == ca:
        return True

    # 7. Jika persis sama
    if ua == ca:
        return True

    return False


# ====== LOGIKA UTAMA KUIS ======
def run_quiz():
    score = 0

    for idx, item in enumerate(questions, start=1):
        print(f"\nSoal {idx}: {item['q']}")
        user_answer = input("Jawab: ")

        if is_correct(user_answer, item["a"]):
            print("Benar!")
            score += 1
        else:
            print(f"Salah! Jawaban yang benar: {item['a'].capitalize()}")

    return score


# ====== PENILAIAN ======
def show_result(score, total):
    print("\n=== HASIL AKHIR ===")
    print(f"Skor Anda: {score}/{total}")

    percent = (score / total) * 100
    print(f"Persentase: {percent:.1f}%")

    if percent == 100:
        print("Sempurna! Kamu benar semua!")
    elif percent >= 70:
        print("Mantap! Pengetahuanmu bagus.")
    elif percent >= 40:
        print("Lumayan, masih perlu belajar.")
    else:
        print("Tetap semangat! Masih bisa lebih baik!")


# ====== FUNGSI UTAMA ======
def main():
    print(f"{APP_NAME} v{APP_VERSION}")
    print("Selamat datang di kuis tebak kota di Jawa Timur!")
    print("----------------------------------------------")
    print("Panduan:")
    print("- Jawablah dengan nama kota.")
    print("- Jawaban boleh panjang (contoh: 'kota malang', 'aku pilih kediri').")
    print("- Hindari kata negasi (contoh: 'bukan kota ...').")
    print("- Hindari simbol seperti !!, ??, %, dll.")
    input("\nTekan Enter untuk memulai kuis...")

    score = run_quiz()
    show_result(score, len(questions))


# ====== EKSEKUSI PROGRAM ======
if __name__ == "__main__":
    main()
