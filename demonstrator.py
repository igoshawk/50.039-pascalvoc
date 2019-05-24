import kivy
import json
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import os
kivy.require('1.9.2')
Window.size = (1500,1000)

import voc_code


class MainScreen(Screen):

    def selected(self, filename):
        self.ids.img.source = filename[0]
        self.ids.pred.text = voc_code.testing('voc_model.pkl', self.ids.img.source)
        #self.ids.pred.text = 'guess what I have predicted'

class AnotherScreen(Screen):
    rank = 0
    data = {}
    flag = False

    def init(self):
        if self.flag == False:
            with open('rank_wempty.txt') as f:
                self.data = json.load(f)

            self.ids.class0.source = self.data['0'][self.rank][0]
            self.ids.class1.source = self.data['1'][self.rank][0]
            self.ids.class2.source = self.data['2'][self.rank][0]
            self.ids.class3.source = self.data['3'][self.rank][0]
            self.ids.class4.source = self.data['4'][self.rank][0]
            self.ids.class5.source = self.data['5'][self.rank][0]
            self.ids.class6.source = self.data['6'][self.rank][0]
            self.ids.class7.source = self.data['7'][self.rank][0]
            self.ids.class8.source = self.data['8'][self.rank][0]
            self.ids.class9.source = self.data['9'][self.rank][0]
            self.ids.class10.source = self.data['10'][self.rank][0]
            self.ids.class11.source = self.data['11'][self.rank][0]
            self.ids.class12.source = self.data['12'][self.rank][0]
            self.ids.class13.source = self.data['13'][self.rank][0]
            self.ids.class14.source = self.data['14'][self.rank][0]
            self.ids.class15.source = self.data['15'][self.rank][0]
            self.ids.class16.source = self.data['16'][self.rank][0]
            self.ids.class17.source = self.data['17'][self.rank][0]
            self.ids.class18.source = self.data['18'][self.rank][0]
            self.ids.class19.source = self.data['19'][self.rank][0]
            self.ids.rank_display.text = 'Rank = %s' %(self.rank+1)

            self.flag = True
    
    def pageup(self):
        if self.rank > 0 and self.flag == True:
            self.rank -= 1

            self.ids.class0.source = self.data['0'][self.rank][0]
            self.ids.class1.source = self.data['1'][self.rank][0]
            self.ids.class2.source = self.data['2'][self.rank][0]
            self.ids.class3.source = self.data['3'][self.rank][0]
            self.ids.class4.source = self.data['4'][self.rank][0]
            self.ids.class5.source = self.data['5'][self.rank][0]
            self.ids.class6.source = self.data['6'][self.rank][0]
            self.ids.class7.source = self.data['7'][self.rank][0]
            self.ids.class8.source = self.data['8'][self.rank][0]
            self.ids.class9.source = self.data['9'][self.rank][0]
            self.ids.class10.source = self.data['10'][self.rank][0]
            self.ids.class11.source = self.data['11'][self.rank][0]
            self.ids.class12.source = self.data['12'][self.rank][0]
            self.ids.class13.source = self.data['13'][self.rank][0]
            self.ids.class14.source = self.data['14'][self.rank][0]
            self.ids.class15.source = self.data['15'][self.rank][0]
            self.ids.class16.source = self.data['16'][self.rank][0]
            self.ids.class17.source = self.data['17'][self.rank][0]
            self.ids.class18.source = self.data['18'][self.rank][0]
            self.ids.class19.source = self.data['19'][self.rank][0]
            self.ids.rank_display.text = 'Rank = %s' %(self.rank+1)

    def pagedown(self):
        if self.rank < 2054 and self.flag == True:
            self.rank += 1

            self.ids.class0.source = self.data['0'][self.rank][0]
            self.ids.class1.source = self.data['1'][self.rank][0]
            self.ids.class2.source = self.data['2'][self.rank][0]
            self.ids.class3.source = self.data['3'][self.rank][0]
            self.ids.class4.source = self.data['4'][self.rank][0]
            self.ids.class5.source = self.data['5'][self.rank][0]
            self.ids.class6.source = self.data['6'][self.rank][0]
            self.ids.class7.source = self.data['7'][self.rank][0]
            self.ids.class8.source = self.data['8'][self.rank][0]
            self.ids.class9.source = self.data['9'][self.rank][0]
            self.ids.class10.source = self.data['10'][self.rank][0]
            self.ids.class11.source = self.data['11'][self.rank][0]
            self.ids.class12.source = self.data['12'][self.rank][0]
            self.ids.class13.source = self.data['13'][self.rank][0]
            self.ids.class14.source = self.data['14'][self.rank][0]
            self.ids.class15.source = self.data['15'][self.rank][0]
            self.ids.class16.source = self.data['16'][self.rank][0]
            self.ids.class17.source = self.data['17'][self.rank][0]
            self.ids.class18.source = self.data['18'][self.rank][0]
            self.ids.class19.source = self.data['19'][self.rank][0]
            self.ids.rank_display.text = 'Rank = %s' %(self.rank+1)

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file('demonstrator.kv')

class MyApp(App):
    def build(self):
        return presentation

if __name__ == '__main__':
    MyApp().run()