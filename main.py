#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# https://www.hackthissite.org/
host = "137.74.187.102"

port = 443


def portScanner(port):

    if s.connect_ex((host,port)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)

