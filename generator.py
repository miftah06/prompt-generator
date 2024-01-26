import random
import keyword

def generate_keyword_file(filename, num_keywords):
    keyword_list = keyword.kwlist

    # Pastikan num_keywords tidak melebihi panjang keyword_list
    num_keywords = min(num_keywords, len(keyword_list))

    random_keywords = random.sample(keyword_list, num_keywords)

    with open(filename, "w") as file:
        file.write("\n".join(random_keywords))

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

# Baca nilai acak untuk objek dan fitur dari file objek.txt dan fitur.txt
with open("keyword1.txt", "r") as objek_file:
    object_options = objek_file.readlines()

with open("keyword2.txt", "r") as fitur_file:
    features_options = fitur_file.readlines()

# Pilih nilai acak untuk opsi objek dan opsi features
object_option = random.choice(object_options).strip()
features_option = random.choice(features_options).strip()

# Simpan hasil ke dalam file output.txt
with open("output.txt", "w") as file:
    dan = " dan serta "
    jika = "jika hal tersebut berupa"
    for prompt in processed_data:
        output_line = f"{command_option} {specification_option} {dan} {prompt} {jika} {object_option} {features_option} {specification_option} \n"
        file.write(output_line)

print("Output telah dibuat dan disimpan dalam output.txt.")
