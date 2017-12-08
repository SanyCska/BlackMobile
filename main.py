from kivy.app import App
from socket import *
from kivy.uix.floatlayout import FloatLayout

HOST = 'localhost'  # локальный адрес localhost или 127.0.0.1

PORT = 21110  # порт на котором работает сервер

BUFSIZ = 1024

ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)

tcpCliSock.connect(ADDR)  # установка связи с сервером

class AddLocationForm(FloatLayout):

    def send_data(self, data):
        tcpCliSock.send(data.encode())  # отправка данных в bytes
        # print(data)

class MirrorApp(App):
    pass


if __name__ == '__main__':
    MirrorApp().run()
    tcpCliSock.close()