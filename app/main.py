import socket  # noqa: F401


def main():

     pong = "+PONG\r\n"
     server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
     conn, addr = server_socket.accept() # wait for client

     with conn:
          conn.recv(1024)
          conn.send(pong.encode())
if __name__ == "__main__":
    main()
