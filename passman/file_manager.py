import os
import config
import pickle

def password_hash_file_exists():
    return os.path.isfile(config.HASH_FILENAME)

def create_password_hash_file(password_hash):
    with open(config.HASH_FILENAME, 'w') as password_hash_file:
        password_hash_file.write(password_hash)
    return True

def write_vault_file(content={}):
    with open(config.VAULT_FILENAME, 'wb') as vault_file:
        pickle.dump(content, vault_file)
    return True

def read_vault_file():
    with open(config.VAULT_FILENAME, 'rb') as vault_file:
        return pickle.load(vault_file)

def get_password_hash():
    with open(config.HASH_FILENAME, 'r') as password_hash_file:
        return password_hash_file.readline()