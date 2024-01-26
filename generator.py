import random
import keyword

# Fungsi untuk membuat file kata kunci acak
def generate_keyword_file(filename, num_keywords):
    keyword_list = keyword.kwlist

    # Pastikan num_keywords tidak melebihi panjang keyword_list
    num_keywords = min(num_keywords, len(keyword_list))

    random_keywords = random.sample(keyword_list, num_keywords)

    with open(filename, "w") as file:
        file.write("\n".join(random_keywords))

# Fungsi untuk membuat prompt AI dengan input dari dua file kata kunci
def create_prompt(input_file1, input_file2, output_file, command_option, specification_option):
    with open(input_file1, "r") as objek_file:
        object_options = objek_file.readlines()

    with open(input_file2, "r") as fitur_file:
        features_options = fitur_file.readlines()

    with open(output_file, "w") as file:
        dan = " dan serta "
        jika = "jika hal tersebut berupa"
        for prompt in processed_data:
            object_option = random.choice(object_options).strip()
            features_option = random.choice(features_options).strip()
            output_line = f"{command_option} {specification_option} {dan} {prompt} {jika} {object_option} {features_option} {specification_option}\n"
            file.write(output_line)

# Membaca dan menulis file teks dalam Python
def read_and_write_file(input_filename, output_filename):
    with open(input_filename, "r") as input_file:
        input_data = input_file.readlines()

    # Lakukan sesuatu dengan data yang dibaca

    with open(output_filename, "w") as output_file:
        # Lakukan sesuatu dengan data dan tulis ke file keluaran
        output_file.write("Contoh hasil tulisan ke file teks.")

# Generate keyword1.txt dengan 50 kata kunci acak dari modul keyword
generate_keyword_file("keyword1.txt", 50)

# Generate keyword2.txt dengan 50 kata kunci acak dari modul keyword
generate_keyword_file("keyword2.txt", 50)

print("Keyword telah dihasilkan dan disimpan dalam keyword1.txt dan keyword2.txt.")

# Baca isi input.txt dan acak urutannya
with open("input.txt", "r") as file:
    input_data = file.readlines()
    random.shuffle(input_data)

# Opsi pengguna untuk perintah dan spesifikasi
command_option = input("Masukkan opsi perintah: ")
specification_option = input("Masukkan opsi spesifikasi: ")

# Proses input sesuai dengan opsi yang diberikan
processed_data = [line.strip() for line in input_data]

# Membuat prompt AI dengan input dari dua file kata kunci
create_prompt("keyword1.txt", "keyword2.txt", "output.txt", command_option, specification_option)

print("Output telah dibuat dan disimpan dalam output.txt.")
