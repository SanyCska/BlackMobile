# # -*- coding: utf-8 -*-
import json
import socket

host = "192.168.1.68"
# host = "localhost"
port=3000
s=socket.socket()
s.bind((host, port))
s.listen(10)

def server():
        while True:
                c, addr=s.accept()
                print("\nconnection successful with "+str(addr)+"\n\n")
                data=c.recv(1024)
                # decoded_data=data.decode("utf-8")
                decoded_data = data.decode()
                if not decoded_data:
                        print("connection with "+ str(addr)+ " broken\n")
                else:
                        print(json.loads(data.decode()))

server()