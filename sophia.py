import paramiko
from pwn import *


def get_sophia_password(HOST, PORT):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(hostname=HOST, username="hacker", password="havefun!", port=PORT)

    p = log.progress("sophia")
    time.sleep(1)

    # Read hidden password
    stdin, stdout, stderr = ssh.exec_command("cat .myhiddenpazz")
    stdout = stdout.readlines()
    password = "".join(stdout).split()[0]
    p.success(password)
    ssh.close() 

    return password
