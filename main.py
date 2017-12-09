from kivy.app import App
# from socket import *
from kivy.uix.floatlayout import FloatLayout
import socket
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
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
# host = "localhost"
port = 3000


class CustomDropDown(DropDown):
    pass

class AddLocationForm(FloatLayout):

    def send_data(self, data):
        # tcpCliSock.send(data.encode())  # отправка данных в bytes
        # print(data)
        s = socket.socket()
        s.connect((host, port))
        # s = socket.socket()
        # # encoded_msg = bytes(data, "utf-8")
        # s.send(encoded_msg)
        s.send(data.encode())
        s.close()
        del s

class MirrorApp(App):
    dropdown = CustomDropDown()
    mainbutton = Button(text='Hello', size_hint=(0.4, 0.1), pos_hint =  {"x":0.3, "y":0.8})
    mainbutton.bind(on_release=dropdown.open)
    dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))




if __name__ == '__main__':
    MirrorApp().run()
    # tcpCliSock.close()