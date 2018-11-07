#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class loginScreen(Screen):
    #rangr.kv - <loginScreen>
    pass

class homeScreen(Screen):
    #rangr.kv - <homeScreen>
    pass

class rangrApp(App):
    #--declarations--#
    use_kivy_settings = False #determines if Kivy config panel appears

    #--end declarations--#
    
    def build(self): #this determines what loads when the app builds
        config = self.config
        screenManager = ScreenManager(transition=NoTransition())
        screenManager.add_widget(loginScreen(name='login'))
        screenManager.add_widget(homeScreen(name='home'))
        return screenManager
            
    def build_config(self, config):
        config.setdefaults('section1', {
            'key1': 'value1',
            'key2': '42'
        })

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

    def on_config_change(self, config, section, key, value):
        if config is self.config:
            token = (section, key)
            if token == ('section1', 'key1'):
                print('Our key1 has been changed to', value)
            elif token == ('section1', 'key2'):
                print('Our key2 has been changed to', value)

    def submitUsername(self, username):
        print(username)

if __name__ == '__main__':                
    rangrApp().run()

#--Remaining items--#
    #(Mostly in ideal chronological order
    #Set up screen manager to manage additional screens === DONE 2018/11/06
    #Add additional screens at a basic level (no content, just KV and app classes)
    #Package attempt 1
    #Create a MySQL DB to manage data and one table to test connection
    #Build connection to DB to store app data (test with login screen)
    #Package attempt 2
    #Design schema for DB connection (this can kind of be ad hoc but ideally the mock ups have the info needed)
    #Begin working through remaining screens and designing elements
    #Search functionality
    #Pull data from DB to add to certain screens
    #Package attempt 3
    #Make screens look nice
    #Make screens look nicer
    #Package attempt 4
