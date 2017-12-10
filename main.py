from kivy.app import App
# from socket import *
from kivy.uix.floatlayout import FloatLayout
import socket
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
import json


# host = "localhost"
port = 3000


class CustomDropDown(DropDown):
    pass

class AddLocationForm(FloatLayout):
    user = ''
    host = ""
    def send_data(self, data):
        # tcpCliSock.send(data.encode())  # отправка данных в bytes
        # print(data)

        s = socket.socket()
        s.connect((self.host, port))
        # s = socket.socket()
        # # encoded_msg = bytes(data, "utf-8")
        # s.send(encoded_msg)
        b = dict({'destination': self.user, 'text': data})
        s.send(json.dumps(b).encode())
        s.close()
        del s
    def set_user(self, data):
        self.user = data

    def set_ip(self, data):
        self.host = data


class MirrorApp(App):
    pass




if __name__ == '__main__':
    MirrorApp().run()