#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

def p_encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password.decode('utf8')

def p_decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password.encode())
    return decrypted_password.decode('utf8')

def load_key():
    if os.path.exists('key.key'):
        with open('key.key', 'rb') as key_file:
            key = key_file.read()
    else:
        key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)
    return key
#----------------------------------------------------------------
def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            usr, passw = line.rstrip().split(':')
            print(f"Username: {usr}, Password: {p_decrypt_password(passw, load_key())}")

def add():
    username = input("Account Name: ")
    pwd = input("Password: ")
    encrypt_password = p_encrypt_password(pwd, load_key())

    with open('password.txt', 'a') as f:
        f.write(f"{username} : {encrypt_password}\n")
        print("Account added successfully.")


##############################################################
master_pwd = input("Enter your master password: ")
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