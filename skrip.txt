import keyword
import random

def generate_related_keywords(base_keyword, num_keywords):
    related_keywords = set()

    # Menambahkan kata kunci dasar ke dalam set
    related_keywords.add(base_keyword.lower())

    # Menambahkan kata kunci terkait sebanyak yang diinginkan
    while len(related_keywords) < num_keywords:
        # Pilih kata kunci acak dari kata kunci yang ada
        random_keyword = random.choice(list(related_keywords))

        # Dapatkan kata kunci terkait dengan kata kunci acak
        new_keywords = [kw.lower() for kw in keyword.kwlist if kw.lower() not in related_keywords]

        # Periksa apakah daftar tidak kosong sebelum memilih
        if new_keywords:
            related_keywords.add(random.choice(new_keywords))
        else:
            break  # Hentikan loop jika daftar kosong

    return list(related_keywords)

def save_to_file(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(data))

if __name__ == "__main__":
    # Opsi kata kunci dari pengguna
    base_keyword = input("Masukkan kata kunci dasar: ")
    num_related_keywords = 10000  # Minimal 100 kata kunci terkait

    # Hasilkan kata kunci terkait
    related_keywords = generate_related_keywords(base_keyword, num_related_keywords)

    # Pisahkan hasil menjadi dua kalimat secara acak
    random.shuffle(related_keywords)
    mid_index = len(related_keywords) // 2
    fitur_keywords = related_keywords[:mid_index]
    objek_keywords = related_keywords[mid_index:]

    # Simpan kata kunci terkait ke dalam file
    save_to_file("fitur.txt", fitur_keywords)
    save_to_file("objek.txt", objek_keywords)

    print("Data kata kunci terkait telah disimpan dalam fitur.txt dan objek.txt.")
