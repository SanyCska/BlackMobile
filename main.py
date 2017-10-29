from kivy.app import App

from kivy.uix.boxlayout import BoxLayout



class AddLocationForm(BoxLayout):
    def search_location(self):
        print('Button pressed')


class MirrorApp(App):
    pass


if __name__ == '__main__':
    MirrorApp().run()