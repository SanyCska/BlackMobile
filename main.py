from kivy.app import App
# from socket import *
from kivy.uix.floatlayout import FloatLayout
import socket
#
# HOST = 'localhost'  # локальный адрес localhost или 127.0.0.1
#
# PORT = 21110  # порт на котором работает сервер
#
# BUFSIZ = 1024
#
# ADDR = (HOST, PORT)
#
# tcpCliSock = socket(AF_INET, SOCK_STREAM)
#
# tcpCliSock.connect(ADDR)  # установка связи с сервером
host = "192.168.1.68"
port = 3000
s = socket.socket()


class AddLocationForm(FloatLayout):

    def send_data(self, data):
        # tcpCliSock.send(data.encode())  # отправка данных в bytes
        # print(data)
        # s = socket.socket()
        # s.connect((host, port))
        s = socket.socket()
        encoded_msg = bytes(data, "utf-8")
        s.send(encoded_msg)
        s.close()

class MirrorApp(App):
    pass




if __name__ == '__main__':
    MirrorApp().run()
    # tcpCliSock.close()