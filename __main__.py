import tkinter as tk
from tkinter import filedialog, messagebox
import random
import os

def generate_key():
    return random.randint(1, 1000)
def encrypt_text():
    text = entry_text.get()
    key = generate_key()
    encrypted_text = yusuf_ozdemir(text, key)

save_encryption_to_file(encrypted_text, key)

    entry_result.delete(0, tk.END)
    entry_result.insert(0, f"Encrypted Text: {encrypted_text} | Key: {key}")

def save_encryption_to_file(encrypted_text, key):
    with open("encrypted_text.txt", "w") as file:
        file.write(f"Encrypted Text: {encrypted_text}\n")
        file.write(f"Key: {key}\n")
    messagebox.showinfo("Saved ", "Encrypted text and key saved to 'encrypted_text.txt'")
def yusuf_ozdemir(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.isupper():
                new_char = chr((ord(char) + shift - 65) % 26 + 65)
            else:
                new_char = chr((ord(char) + shift - 97) % 26 + 97)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text
def decrypt_text():
    file_path = filedialog.askopenfilename(title="Select the encrypted file", filetypes=(("Text Files", "*.txt"),))

    if not file_path:
        return

    with open(file_path, "r") as file:
        lines = file.readlines()
        encrypted_text = lines[0].split(": ")[1].strip()
        key = int(lines[1].split(": ")[1].strip())
    decrypted_text = yusuf_ozdemir(encrypted_text, -key)
    entry_result.delete(0, tk.END)
    entry_result.insert(0, f"Decrypted Text: {decrypted_text}")
root = tk.Tk()
root.title("Secret Notes Homework")

label_text = tk.Label(root, text="Enter Text:")
label_text.grid(row=0, column=0)

entry_text = tk.Entry(root, width=50)
entry_text.grid(row=0, column=1)

button_encrypt = tk.Button(root, text="Encrypt and Save", command=encrypt_text)
button_encrypt.grid(row=1, column=1)

button_decrypt = tk.Button(root, text="Decrypt", command=decrypt_text)
button_decrypt.grid(row=2, column=1)

label_result = tk.Label(root, text="Result:")
label_result.grid(row=3, column=0)

entry_result = tk.Entry(root, width=50)
entry_result.grid(row=3, column=1)

root.mainloop()

























































































tkinter.mainloop()