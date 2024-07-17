#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet
import base64
import hashlib

class PasswordManager:
    def __init__(self, master_password):
        self.master_password_hash = self.load_master_password_hash()
        if not self.verify_master_password(master_password):
            print("Incorrect master password. Exiting.")
            exit()
        self.key = self.load_key(master_password)
        self.file_path = 'password.txt'

    def load_master_password_hash(self):
        """Loads the hashed master password from a file."""
        hash_file = 'master_password.hash'
        if os.path.exists(hash_file):
            with open(hash_file, 'rb') as f:
                return f.read()
        else:
            return None

    def save_master_password_hash(self, master_password):
        """Saves the hashed master password to a file."""
        hash_file = 'master_password.hash'
        hashed_password = hashlib.sha256(master_password.encode()).digest()
        with open(hash_file, 'wb') as f:
            f.write(hashed_password)

    def verify_master_password(self, master_password):
        """Verifies the entered master password against the stored hash."""
        if self.master_password_hash is None:
            # First-time setup
            self.save_master_password_hash(master_password)
            return True
        else:
            entered_password_hash = hashlib.sha256(master_password.encode()).digest()
            return entered_password_hash == self.master_password_hash

    def load_key(self, master_password):
        """Generates or loads a key and combines it with the master password."""
        key_file = 'key.key'
        if os.path.exists(key_file):
            with open(key_file, 'rb') as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, 'wb') as f:
                f.write(key)
        
        master_password = hashlib.sha256(master_password.encode()).digest()
        combined_key = base64.urlsafe_b64encode(master_password + key[:16])
        return combined_key

    def encrypt_password(self, password):
        """Encrypts a password."""
        f = Fernet(self.key)
        encrypted_password = f.encrypt(password.encode())
        return encrypted_password.decode('utf-8')

    def decrypt_password(self, encrypted_password):
        """Decrypts a password."""
        f = Fernet(self.key)
        decrypted_password = f.decrypt(encrypted_password.encode())
        return decrypted_password.decode('utf-8')

    def add_account(self, username, password):
        """Adds a new account with encrypted password."""
        encrypted_password = self.encrypt_password(password)
        with open(self.file_path, 'a') as f:
            f.write(f"{username}:{encrypted_password}\n")
        print("Account added successfully.")

    def view_accounts(self):
        """Prints the existing accounts with decrypted passwords."""
        if not os.path.exists(self.file_path):
            print("No accounts found.")
            return

        with open(self.file_path, 'r') as f:
            for line in f:
                usr, passw = line.rstrip().split(':')
                decrypted_password = self.decrypt_password(passw)
                print(f"Username: {usr}, Password: {decrypted_password}")

def main():
    master_password = input("Enter your master password: ")
    manager = PasswordManager(master_password)

    while True:
        mode = input("Add new password or View existing passwords [view, add, exit]: ").lower()
        if mode == "view":
            manager.view_accounts()
        elif mode == "add":
            username = input("Account Name: ")
            password = input("Password: ")
            manager.add_account(username, password)
        elif mode == "exit":
            break
        else:
            print("Invalid mode. Please enter 'view', 'add', or 'exit'.")

if __name__ == "__main__":
    main()
