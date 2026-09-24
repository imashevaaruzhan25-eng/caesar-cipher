alphabet = "abcdefghijklmnopqrstuvwxyz"

word = input("Введите слово: ")
key = int(input("Введите ключ: "))

# Шифрование
encrypted = ""

for letter in word:
    if letter in alphabet:
        position = alphabet.index(letter)
        new_position = (position + key) % 26
        encrypted += alphabet[new_position]
    else:
        encrypted += letter

print("Зашифрованное слово:", encrypted)

# Расшифровка
decrypted = ""

for letter in encrypted:
    if letter in alphabet:
        position = alphabet.index(letter)
        new_position = (position - key) % 26
        decrypted += alphabet[new_position]
    else:
        decrypted += letter

print("Расшифрованное слово:", decrypted)
