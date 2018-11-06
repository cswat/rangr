from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class loginScreen(BoxLayout):
    #<loginScreen>
    pass

class homepage(Widget):
    pass

class rangrApp(App):
    #--declarations--#
    use_kivy_settings = False #determines if Kivy config panel appears


    #--end declarations--#
    
    def build_config(self, config):
        config.setdefaults('section1', {
            'key1': 'value1',
            'key2': '42'
        })
 
    def build(self):
        config = self.config
        if True == True:
            return loginScreen()
        else:
            return homepage()

    def build_settings(self, settings):
        jsondata = """[
            { "type": "title",
              "title": "Test application" },

            { "type": "options",
              "title": "My first key",
              "desc": "Description of my first key",
              "section": "section1",
              "key": "key1",
              "options": ["value1", "value2", "another value"] },

            { "type": "numeric",
              "title": "My second key",
              "desc": "Description of my second key",
              "section": "section1",
              "key": "key2" }
        ]"""
        settings.add_json_panel('Test application',
            self.config, data=jsondata)
        
    def submitUsername(username):
        print(username)

    def on_config_change(self, config, section, key, value):
        if config is self.config:
            token = (section, key)
            if token == ('section1', 'key1'):
                print('Our key1 has been changed to', value)
            elif token == ('section1', 'key2'):
                print('Our key2 has been changed to', value)

if __name__ == '__main__':                
    rangrApp().run()

