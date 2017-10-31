from kivy.app import App
from socket import *
from kivy.uix.boxlayout import BoxLayout



class AddLocationForm(BoxLayout):
    def client_start(self):
        HOST = 'localhost'  # локальный адрес localhost или 127.0.0.1

        PORT = 21111  # порт на котором работает сервер

        BUFSIZ = 1024

        ADDR = (HOST, PORT)

        tcpCliSock = socket(AF_INET, SOCK_STREAM)

        tcpCliSock.connect(ADDR)  # установка связи с сервером

        while True:

            data = input('>')  # ввод данных для отправки

            if not data:
                break

            tcpCliSock.send(data.encode())  # отправка данных в bytes

            data = tcpCliSock.recv(BUFSIZ)  # ожидание (получение) ответа

            if not data:
                break

            print(data.decode('utf8'))

        tcpCliSock.close()


class MirrorApp(App):
    pass


if __name__ == '__main__':
    MirrorApp().run()