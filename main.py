from kivy.app import App
from socket import *
from kivy.uix.boxlayout import BoxLayout

HOST = 'localhost'  # локальный адрес localhost или 127.0.0.1

PORT = 21110  # порт на котором работает сервер

BUFSIZ = 1024

ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)

tcpCliSock.connect(ADDR)  # установка связи с сервером

class AddLocationForm(BoxLayout):
    def client_start1(self):
        # while True:
        # data = input('>')  # ввод данных для отправки
        data = '1'
        # if not data:
        #     break
        tcpCliSock.send(data.encode())  # отправка данных в bytes

        # data = tcpCliSock.recv(BUFSIZ)  # ожидание (получение) ответа
        #
        # if not data:
        #     break
        # print(data.decode('utf8'))
    def client_start2(self):
        data = 'Moscow'
        tcpCliSock.send(data.encode())  # отправка данных в bytes

class MirrorApp(App):
    pass


if __name__ == '__main__':
    MirrorApp().run()
    tcpCliSock.close()