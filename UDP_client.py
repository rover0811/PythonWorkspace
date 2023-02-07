import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 16002
MESSAGE = 'Hello, donghyun!'

print('UDP target IP', UDP_IP)
print('UDP target port', UDP_PORT)
print('Message', MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 소켓 생성
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
modifiedData = sock.recv(1024)
print(modifiedData)

sock.close()
