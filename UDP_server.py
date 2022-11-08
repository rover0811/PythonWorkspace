import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 16002

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 소켓 생성

sock.bind((UDP_IP, UDP_PORT))  # 바인드하기

while True:  # 무한루프
    data, addr = sock.recvfrom(1024)
    print("Connected by", addr)
    modifiedData = data.decode().upper()
    print('Received message', data)
    sock.sendto(modifiedData.encode(), addr)
