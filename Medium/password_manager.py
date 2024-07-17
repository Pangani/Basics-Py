#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet
import hashlib

################################################################
# 
def p_encrypt_password(password, key):
    """Returns encrpted password"""
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password.decode('utf8')

def p_decrypt_password(encrypted_password, key):
    """Returns decrypted password"""
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password.encode())
    return decrypted_password.decode('utf8')

def load_key():
    """Returns key from cryptography"""
    if os.path.exists('key.key'):
        with open('key.key', 'rb') as key_file:
            key = key_file.read()
    else:
        key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)
    return key

#----------------------------------------------------------------
# Save and Verify the master password
def load_master_password_hash():
    """Loads the hashed master password from a file."""
    hash_file = 'master_password.hash'
    if os.path.exists(hash_file):
        with open(hash_file, 'rb') as f:
            return f.read()
    else:
        return None

def save_master_password_hash(master_password):
    """Saves the hashed master password to a file."""
    hash_file = 'master_password.hash'
    hashed_password = hashlib.sha256(master_password.encode()).digest()
    with open(hash_file, 'wb') as f:
        f.write(hashed_password)

def verify_master_password(master_password, master_password_hash):
    """Verifies the entered master password against the stored hash."""
    if master_password_hash is None:
        # First-time setup
        save_master_password_hash(master_password)
        return True
    else:
        entered_password_hash = hashlib.sha256(master_password.encode()).digest()
        return entered_password_hash == master_password_hash
#----------------------------------------------------------------
def view():
    """Prints the existing accounts"""
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            usr, passw = line.rstrip().split(':')
            print(f"Username: {usr}, Password: {p_decrypt_password(passw, load_key())}")

def add():
    """Adds a new account"""
    username = input("Account Name: ")
    pwd = input("Password: ")
    encrypt_password = p_encrypt_password(pwd, load_key())

    with open('password.txt', 'a') as f:
        f.write(f"{username} : {encrypt_password}\n")
        print("Account added successfully.")


##############################################################
master_pwd = input("Enter your master password: ")
kept_master_password = load_master_password_hash()

if master_pwd is None or not verify_master_password(master_pwd, kept_master_password):
    print("Incorrect master password.")
    exit(1)
key = load_key() + bytes(master_pwd, 'utf-8')

while True:
    mode = input("Add new password or  View existing password [view, add]: ")

    if mode.lower() not in ["view", "add"]:
        print("Invalid mode. Please enter 'view' or 'add'.")
        break

    if mode.lower() == "view":
        view()
    elif mode.lower() == "add":
        add()