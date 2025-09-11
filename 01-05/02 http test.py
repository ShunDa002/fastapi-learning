# Web App follows http protocol
import socket

sock = socket.socket()

sock.bind(("127.0.0.1", 8080))
sock.listen(5)
while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print("Data from client:\n", data)
    # No format
    # conn.send(b"Hello world")
    # Http format:  #   1 response Status line
                    #   2 response Headers
                    #   3 response Body
    conn.send(b"HTTP/1.1 200 ok\r\ncontent-type:text/plain\r\n\r\n<h1>Hello world<h1>")
    conn.close()
    
