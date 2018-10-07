import re
import getpass
import hashlib
import binascii

# Taken from https://stackoverflow.com/questions/16709638/checking-the-strength-of-a-password-how-to-check-conditions
def check_password_strength(password):
    """
    Verify the strength of 'password'
    Returns a dict indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """

    # calculating the length
    length_error = len(password) < 8

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # searching for symbols
    symbol_error = re.search(r"[ !#$@?%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None

    # overall result
    password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error or symbol_error )

    return {
        'password_ok' : password_ok,
        'length_error' : length_error,
        'digit_error' : digit_error,
        'uppercase_error' : uppercase_error,
        'lowercase_error' : lowercase_error,
        'symbol_error' : symbol_error,
    }

def generate_password_error(password_checks):
    print("Invalid password, please correct the following errors:")
    if(password_checks['length_error']):
        print("Password length must be at least 8 characters")
    if(password_checks['digit_error']):
        print("Password must contain at least one digit")
    if(password_checks['uppercase_error']):
        print("Password must contain at least one uppercase letter")
    if(password_checks['lowercase_error']):
        print("Password must contain at least one lowercase letter")
    if(password_checks['symbol_error']):
        print("Password must contain at least one special character")

def get_master_password(init=False):
    password = getpass.getpass("Enter the master password: ")
    if init:
        password_checks = check_password_strength(password)
        if not (password_checks['password_ok']):
            generate_password_error(password_checks)
            exit()
        print("Password OK")
    return password

def get_master_password_hash(init=False):
    password = get_master_password(init)
    password_pbkdf2 = hashlib.pbkdf2_hmac('sha256', str.encode(password), b'', 100000)
    password_pbkdf2 = binascii.hexlify(password_pbkdf2).decode()
    return password_pbkdf2

def compare_password_hashes(supplied_password_hash, stored_password_hash):
    return supplied_password_hash == stored_password_hash