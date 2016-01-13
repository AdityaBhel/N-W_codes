# Tcp echo server
import socket


def echo(y):
    print "waiting for the client  "
    (client, (ip, port)) = y.accept()
    print "received connection from ", ip
    print "Server ready for echo  "
    dummy = "0000"
    while len(dummy):
        dummy = client.recv(2048)
        client.send("SERVER:" + dummy)
    print("blank request closing connection for the client ")
    client.close()


def start():
    tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsocket.bind(("0.0.0.0", 8000))
    tcpsocket.listen(2)
    return tcpsocket


def server():
    x = start()
    echo(x)
    while raw_input("connect more clients press any key") is not None:
        echo(x)
    x.close()


def main():
    server()


if __name__ == '__main__':
    main()

"""
to run open terminal use
ifconfig  find out the interface ip
do
nc interface_ip 8000
"""
