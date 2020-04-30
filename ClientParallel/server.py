import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

l = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            elif (data == b'stop server'):
                conn.sendall(b'the server was stopped')
                break
            elif (data == b'clear'):
                l = []
                conn.sendall(b'list was cleared')
            elif (data == b'list'):
                c = b'All message :'
                for i in l:
                    c = c+i+b', '
                conn.sendall(c)
            else:
                l.append(data)
                conn.sendall(data)
