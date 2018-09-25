from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()


#got it working via:
#https://kivy.org/doc/stable/installation/installation-windows.html#installation
