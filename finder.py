import random

# Baca isi prompt dari input.txt
with open("output.txt", "r") as file:
    prompt_text = file.read()

# Pisahkan setiap kalimat prompt
prompt_sentences = prompt_text.split(".")

# Acak urutan kalimat
random.shuffle(prompt_sentences)

# Gabungkan kembali kalimat-kalimat yang sudah diacak
shuffled_prompt = ".".join(prompt_sentences)

# Tulis prompt yang sudah diacak ke dalam file output.txt
with open("hasil.txt", "w") as file:
    file.write(shuffled_prompt)

# Tampilkan prompt yang sudah diacak
print("Shuffled AI Prompt Text:")
print(shuffled_prompt)
