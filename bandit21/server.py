#!/usr/bin/env python3

import socket

HOST = '127.0.0.1' 
PORT = 4444
PASSWORD = 'GbKksEFF4yrVs6il55v6gwY5aVje5f0j'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        conn.sendall(bytes(PASSWORD, "utf-8"))
        data = conn.recv(1024)
        print(data)