import argparse
import config
import file_manager
import password_ops
import secrets
import string

def init():
    if file_manager.password_hash_file_exists():
        answer = input("Initialization will PERMANENTLY delete all existing records, proceed? [y/N] ")
        if answer.lower() != 'y':
            exit()
    password_hash = password_ops.get_master_password_hash(True)
    if file_manager.create_password_hash_file(password_hash) and file_manager.write_vault_file():
        del password_hash
        print("Initialization successful")
    else:
        print("PassMan initialization failed")
    
def prompt_for_init():
    answer = input("PassMan was not initialized, initialize ? [Y/n] ")
    if answer.lower() == 'n':
        exit()
    init()
    exit()

def validate_password_hash(supplied_password_hash):
    if password_ops.compare_password_hashes(supplied_password_hash, file_manager.get_password_hash()):
        print("Password OK")
        del supplied_password_hash
    else:
        print("Incorrect master password")
        exit()

def get_service_password(service_name):
    if not file_manager.password_hash_file_exists():
        prompt_for_init()
    supplied_password_hash = password_ops.get_master_password_hash()
    validate_password_hash(supplied_password_hash)
    # Add logic

def add_service_password(service_name):
    if not file_manager.password_hash_file_exists():
        prompt_for_init()
    supplied_password_hash = password_ops.get_master_password_hash()
    validate_password_hash(supplied_password_hash)
    alphabet = string.printable
    password = ''.join(secrets.choice(alphabet) for i in range(config.PASSWORD_LENGTH))
    print(file_manager.read_vault_file())

"""
Checks supplied arguments
"""
def check_args(args):
    if args['i']:
        init()
        exit()
    if args['g']:
        get_service_password(args['g'])
    if args['n']:
        add_service_password(args['n'])

"""
The script starts here, initializes accepted arguments and calls check_args()
""" 
def run():
    parser = argparse.ArgumentParser(description='PassMan: Password Manager')
    parser.add_argument('-i', '-init', help='Initialize PassMan', action='store_true')
    parser.add_argument('-g', '-get', help="Get supplied service's password")
    parser.add_argument('-n', '-new', help="Generate new password for the supplied service")
    args = vars(parser.parse_args())
    check_args(args)

run()