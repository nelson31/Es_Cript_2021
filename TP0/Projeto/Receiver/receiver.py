import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
SOCKET_READ_BLOCK_LEN = 4096  # bytes


def communicate():
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP

    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(SOCKET_READ_BLOCK_LEN)
        print("received from ", str(addr[0]), " message: ", data)


def main():
    communicate()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

