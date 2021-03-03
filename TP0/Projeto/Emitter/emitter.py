import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = b"Hello, World!"
SOCKET_READ_BLOCK_LEN = 4096  # bytes


def communicate():
    print("UDP target IP: %s" % UDP_IP)
    print("UDP target port: %s" % UDP_PORT)
    print("message: %s" % MESSAGE)

    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP

    while True:
        pt = input("Client message: ")
        if len(pt) > 0:
            sock.sendto(pt.encode("utf-8"), (UDP_IP, UDP_PORT))
        else:
            sock.close()
            break


def main():
    communicate()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
