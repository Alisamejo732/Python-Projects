from cryptography.fernet import Fernet



# We don't need this function anymore
'''def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)'''

def load_key():
    with open ('key.key', 'rb') as file:
        key = file.read()
    return key



# Logic part
master_pwd = input('What is the master password: ')
# write_key() # Calling it only one as it'll create key inside key.key file
key = load_key()
fer = Fernet(key)

# Functions
def add_password():
    accnt_name = input('Enter the account name: ')
    pwd = input(f'Enter the password for {accnt_name}: ')
    password = fer.encrypt(f'{pwd}'.encode()).decode()

    with open('passwords.txt', 'a') as file:
        file.write(accnt_name + "|" + password + '\n')
    print('Successfully added new password.')

def view_password():

    with open("passwords.txt", 'r') as file:
        for line in file.readlines():
            data = line.strip()
            name, pwd = data.split('|')
            print(f'Username: {name}, Password = {fer.decrypt(pwd.encode()).decode()}')


while True:
    mode = input('Would you like to add a new password or view exiting ones view|add or \'q\' to exit: ')

    if mode.lower() == 'q':
        break

    if mode.lower() == 'view':
        data = view_password()
        print(data)
    elif mode.lower() == 'add':
        add_password()
    else:
        print('Invalid mode..')
        continue

