from sophia import get_sophia_password
from angela import get_angela_password
from emma import get_emma_password

HOST = "venus.hackmyvm.eu"
PORT = 5000

def main():
    sophia_password = get_sophia_password(HOST, PORT)
    angela_password = get_angela_password(HOST, PORT, sophia_password)
    emma_password = get_emma_password(HOST, PORT, angela_password)
    return

if __name__ == '__main__':
    main()