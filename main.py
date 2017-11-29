from kivy.app import App
from kivy.core.window import Window
from socket import *
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

HOST = 'localhost'  # локальный адрес localhost или 127.0.0.1

PORT = 21112  # порт на котором работает сервер

BUFSIZ = 1024

ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)

tcpCliSock.connect(ADDR)  # установка связи с сервером

class MyApp(App):
# layout
    def build(self):
        #layout = BoxLayout(padding=10, orientation='vertical')
        layout = FloatLayout()
        print (Window.size)
        layout1 = AnchorLayout(anchor_x='center', anchor_y='bottom')
        btn1 = Button(text="OK",size_hint=(.5, .1))
        btn1.bind(on_press=self.buttonClicked)
        layout1.add_widget(btn1)
        layout2 = AnchorLayout(anchor_x='center', anchor_y='top')
        # self.lbl1 = Label(text="test")
        # layout2.add_widget(self.lbl1)
        self.txt1 = TextInput(text='', multiline=False, size_hint=(.8, .8))
        layout2.add_widget(self.txt1)
        layout.add_widget(layout1)
        layout.add_widget(layout2)
        return layout

# button click function
    def buttonClicked(self,btn):
        tcpCliSock.send(self.txt1.text.encode())

# run app
if __name__ == "__main__":
    # Window.fullscreen = 'auto'
    MyApp().run()
    tcpCliSock.close()

# class MainScreen(BoxLayout):
#     def __init__(self, **kwargs):
#         super(MainScreen, self).__init__(**kwargs)
#         layout = BoxLayout(padding=10, orientation='vertical')
#         btn1 = Button(text="OK")
#         btn1.bind(on_press=self.buttonClicked)
#         layout.add_widget(btn1)
#         lbl1 = Label(text="test")
#         layout.add_widget(lbl1)
#         txt1 = TextInput(text='', multiline=False)
#         layout.add_widget(txt1)
#         print(layout)
#
#     # button click function
#     def buttonClicked(self, btn):
#         lbl1.text = "You wrote " + txt1.text


# class AddLocationForm(BoxLayout):
#     def client_start1(self):
#         # while True:
#         # data = input('>')  # ввод данных для отправки
#         data = '1'
#         # if not data:
#         #     break
#         tcpCliSock.send(data.encode())  # отправка данных в bytes
#
#         # data = tcpCliSock.recv(BUFSIZ)  # ожидание (получение) ответа
#         #
#         # if not data:
#         #     break
#         # print(data.decode('utf8'))
#     def client_start2(self):
#         data = 'Moscow'
#         tcpCliSock.send(data.encode())  # отправка данных в bytes
#
#
# class MirrorApp(App):
#     # def build(self):
#     #     return MainScreen()
#     pass
#
#
# if __name__ == '__main__':
#     MirrorApp().run()
#     tcpCliSock.close()