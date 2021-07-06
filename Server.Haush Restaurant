import socket
import sys
import time
import errno
import math
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 NotFound\n\n'

def process_start(s_sock,s_addr):
    s_sock.send(str.encode('Welcome to the Haush Restaurant ^_^\n'))
    while True:
        data = str(s_sock.recv(2048).decode())
        print(data)
        op,tabl,quant,totp = data.split('.')
        if op == "BA":
            print(str(s_addr) + "Meja " + tabl + " Ordered " + quant + " Bubur Ayam ")
            line = "\n_____________________________________________________________\n"

            haush = "\nTotal Price : RM" + totp + line
            s_sock.send(str.encode(haush))
        elif op == "IBC":
            print(str(s_addr) + "Meja " + tabl + " Ordered " + quant + " Ice Blended Chocolate")
            line = "\n__________________________________________________________\n"

            haush = "\nTotal Price : RM" + totp + line
            s_sock.send(str.encode(haush))
        elif op == "IBS":
            print(str(s_addr) + "Meja " + tabl + " Ordered " + quant + " Ice Blended Strawberry")
            line = "\n______________________________________________________________\n"

            haush = "\nTotal Price : RM" + totp + line
            s_sock.send(str.encode(haush))
        elif op == "Q":
            print(str(s_addr) + "Itu Saje")
            s_sock.close()
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,s_addr))
                p.start()

            except socket.error:

                print('socket error')

    except Exception as e:
        print('an exception occurred!')
        print(e)
        sys.exit(1)
    finally:
     	s.close()
