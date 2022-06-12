# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import socket


def send_udp_message(message):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(message.encode(), ("166.111.50.194", 10053))
    udp_socket.close()


def receive_udp_message(message):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(message.encode(), ("166.111.50.194", 10053))
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data[0].decode())
    udp_socket.close()


def send_udp_message_with_constant_port(message):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("183.173.81.27", 8080))
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
    udp_socket.sendto(message.encode(), ("255.255.255.255", 10053))
    udp_socket.close()


def receive_udp_message_with_constant_port():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("183.173.81.27", 8080))
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data[0].decode())
    udp_socket.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # send_udp_message('PyCharm')
    send_udp_message_with_constant_port('This is a test!')
    # receive_udp_message_with_constant_port()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
