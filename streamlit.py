import streamlit as st
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import string
import random

def generate_key_from_password(password):
    # Menggunakan PBKDF2 untuk menghasilkan kunci dari password
    salt = b'salt_'  # Dalam praktik nyata, gunakan salt yang random
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                shifted = (ord(char) - ascii_offset + shift) % 26
            else:
                shifted = (ord(char) - ascii_offset - shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    st.title("Aplikasi Kriptografi Sederhana")
    
    menu = ["Enkripsi/Dekripsi Modern", "Caesar Cipher", "Generator Password"]
    choice = st.sidebar.selectbox("Pilih Metode", menu)
    
    if choice == "Enkripsi/Dekripsi Modern":
        st.subheader("Enkripsi/Dekripsi Menggunakan Fernet")
        
        # Input teks dan password
        message = st.text_area("Masukkan Pesan")
        password = st.text_input("Masukkan Password", type="password")
        
        if st.button("Enkripsi"):
            if message and password:
                try:
                    key = generate_key_from_password(password)
                    encrypted_message = encrypt_message(message, key)
                    st.success("Pesan Terenkripsi:")
                    st.code(encrypted_message.decode())
                except Exception as e:
                    st.error(f"Terjadi kesalahan: {str(e)}")
        
        # Dekripsi
        encrypted_input = st.text_area("Masukkan Pesan Terenkripsi")
        decrypt_password = st.text_input("Masukkan Password untuk Dekripsi", type="password")
        
        if st.button("Dekripsi"):
            if encrypted_input and decrypt_password:
                try:
                    key = generate_key_from_password(decrypt_password)
                    decrypted_message = decrypt_message(encrypted_input.encode(), key)
                    st.success("Pesan Terdekripsi:")
                    st.write(decrypted_message)
                except Exception as e:
                    st.error("Password salah atau format pesan tidak valid")
    
    elif choice == "Caesar Cipher":
        st.subheader("Caesar Cipher")
        
        text = st.text_area("Masukkan Teks")
        shift = st.number_input("Masukkan Jumlah Pergeseran", min_value=1, max_value=25, value=3)
        cipher_mode = st.radio("Pilih Mode", ['Enkripsi', 'Dekripsi'])
        
        if st.button("Proses"):
            if text:
                mode = 'encrypt' if cipher_mode == 'Enkripsi' else 'decrypt'
                result = caesar_cipher(text, shift, mode)
                st.success(f"Hasil {cipher_mode}:")
                st.code(result)
    
    elif choice == "Generator Password":
        st.subheader("Generator Password")
        
        length = st.slider("Panjang Password", 8, 32, 12)
        if st.button("Generate Password"):
            password = generate_password(length)
            st.success("Password yang Dihasilkan:")
            st.code(password)

if __name__ == '__main__':
    main()
