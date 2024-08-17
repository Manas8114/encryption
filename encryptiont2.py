import tkinter as tk
from tkinter import filedialog, messagebox
import random
import string
import os

class FileEncryptorDecryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryptor & Decryptor")

        # Generate Key
        self.key = self.generate_key()

        # UI Setup
        self.encrypt_button = tk.Button(root, text="Encrypt File", command=self.encrypt_file)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = tk.Button(root, text="Decrypt File", command=self.decrypt_file)
        self.decrypt_button.pack(pady=10)

    def generate_key(self):
        chars = " " + string.punctuation + string.digits + string.ascii_letters
        chars = list(chars)
        key = chars.copy()
        random.shuffle(key)
        return key

    def encrypt_file(self):
        file_path = filedialog.askopenfilename(title="Select File to Encrypt")
        if not file_path:
            return

        encrypted_file_path = file_path + ".enc"

        try:
            with open(file_path, 'rb') as file:
                plain_data = file.read()

            encrypted_data = bytearray()
            for byte in plain_data:
                index = self.key.index(chr(byte))
                encrypted_data.append(ord(self.key[index]))

            with open(encrypted_file_path, 'wb') as file:
                file.write(encrypted_data)

            messagebox.showinfo("Success", f"File encrypted successfully. Encrypted file saved as: {encrypted_file_path}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def decrypt_file(self):
        encrypted_file_path = filedialog.askopenfilename(title="Select File to Decrypt")
        if not encrypted_file_path:
            return

        decrypted_file_path = os.path.splitext(encrypted_file_path)[0]

        try:
            with open(encrypted_file_path, 'rb') as file:
                encrypted_data = file.read()

            decrypted_data = bytearray()
            for byte in encrypted_data:
                index = self.key.index(chr(byte))
                decrypted_data.append(ord(self.key[index]))

            with open(decrypted_file_path, 'wb') as file:
                file.write(decrypted_data)

            messagebox.showinfo("Success", f"File decrypted successfully. Decrypted file saved as: {decrypted_file_path}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileEncryptorDecryptorApp(root)
    root.mainloop()
