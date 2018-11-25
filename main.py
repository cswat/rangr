#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from kivy.garden.navigationdrawer import NavigationDrawer ##Uncomment later

class loginScreen(Screen):
    #rangr.kv - <loginScreen>
    pass

class homeScreen(Screen):
    #rangr.kv - <homeScreen>
    pass

class userProfileScreen(Screen):
    #rangr.kv - <userProfileScreen>
    pass

class searchResultsScreen(Screen):
    #rangr.kv - <searchResultsScreen>
    pass

class addNewParkScreen(Screen):
    #rangr.kv - <addNewParkScreen>
    pass

class viewParkScreen(Screen):
    #rangr.kv - <viewParkScreen>
    pass

class makeReportScreen(Screen):
    #rangr.kv - <makeReportScreen>
    pass

class appInfoScreen(Screen):
    #rangr.kv - <appInfoScreen>
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
        screenManager.add_widget(userProfileScreen(name='userProfile'))
        screenManager.add_widget(searchResultsScreen(name='searchResults'))
        screenManager.add_widget(addNewParkScreen(name='addNewPark'))
        screenManager.add_widget(viewParkScreen(name='viewPark'))
        screenManager.add_widget(makeReportScreen(name='makeReport'))
        screenManager.add_widget(appInfoScreen(name='appInfo'))
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
    #(Mostly in ideal chronological order)
    #Set up screen manager to manage additional screens === DONE 2018/11/06
    #Add additional screens at a basic level (no content, just KV and app classes) === DONE 2018/11/07
    #Package attempt 1 == DONE 2018/11/14
    #Build hamburger menu == DONE 2018/11/25
    #Flesh out additional screens with content
    #Create a MySQL DB to manage data and one table to test connection
    #Figure out what MySQL connector to use (PyMySQL vs mysqlclient) === DONE 2018/11/18
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
