import socket
import math

ClientSocket = socket.socket()
host = '192.168.43.38'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
    print('Connected!!')
except socket.error as ex:
    print(str(ex))

Response = ClientSocket.recv(1024).decode()
print(Response)

while True:
    print (' BA - Bubur Ayam \n IBC - Ice Blended Chocolate \n IBS - Ice Blended Strawberry \n Q - Quit')
    meja = input('\nMasukkan Nombor Meja : ')
    Input = input('\nOrder makanan anda : ')
    
    if Input == 'BA' :
        option = "BA"
        meja = meja
        quantity = input('Quantity : ')
        quantity = int(quantity)
        totharga = 5*quantity
        l = option + '.' + str(meja) + '.' + str(quantity) + '.' + str(totharga)
        ClientSocket.send(str.encode(l))
    elif Input == 'IBC':
        option = "IBC"
        meja = meja
        quantity = input('Quantity : ')
        quantity = int(quantity)
        totharga = 2.5*quantity
        s = option + '.' + str(meja) + '.' + str(quantity) + '.' + str(totharga)
        ClientSocket.send(str.encode(s))
    elif Input == 'IBS':
        option = "IBS"
        meja = meja
        quantity = input('Quantity : ')
        quantity = int(quantity)
        totharga = 3*quantity
        e = option + '.' + str(meja) + '.' + str(quantity) + '.' + str(totharga)
        ClientSocket.send(str.encode(e))
    elif Input == "Q":
        option = "Q"
        meja = "0"
        quantity = "0"
        totharga = "0"
        f = option + '.' + str(meja) + '.' + str(quantity) + '.' + str(totharga)
        ClientSocket.send(str.encode(f))
        print ('TERIMA KASIH, JUMPA LAGI!! \n')
        ClientSocket.close()
    else :
        print ('Pesanan tidak wujud! Sila Gunakan Keyword BA, IBC atau IBS sahaja\n')
        
    Response = ClientSocket.recv(1024)
    print(Response.decode())

ClientSocket.close()
