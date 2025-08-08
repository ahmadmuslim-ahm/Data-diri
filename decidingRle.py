def rle_encode(data):
    encoding = ''
    if not data:
        return ''
    
    prev_char = data[0]
    count = 1

    for char in data[1:]:
        if char == prev_char:
            count += 1
        else:
            encoding += str(count) + prev_char
            prev_char = char
            count = 1
    encoding += str(count) + prev_char
    return encoding

def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

# Membaca isi file input.txt
with open('input.txt', 'r') as file:
    text = file.read().strip()

# Kompresi
encoded_text = rle_encode(text)
print("Hasil Kompresi:", encoded_text)

# Menyimpan hasil kompresi
with open('encoded.txt', 'w') as file:
    file.write(encoded_text)

# Dekompresi
decoded_text = rle_decode(encoded_text)
print("Hasil Dekompresi:", decoded_text)

# Membandingkan ukuran file
import os

original_size = os.path.getsize('input.txt')
compressed_size = os.path.getsize('encoded.txt')

print(f"Ukuran File Asli: {original_size} bytes")
print(f"Ukuran File Kompresi: {compressed_size} bytes")
print(f"Rasio Kompresi: {original_size / compressed_size:.2f}")