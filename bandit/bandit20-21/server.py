#!/usr/bin/env python3

import socket

HOST = '127.0.0.1' # localhost
PORT = 4444 # Change to what ever port you want

# Password for bandit20
PASSWORD = 'GbKksE##########################' 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        conn.sendall(bytes(PASSWORD, "utf-8"))
        data = conn.recv(1024)
        print(data.decode('utf-8'))