from random import uniform
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup



Window.size = (360, 640)
t = 0

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            Color(uniform(0.5, 1), uniform(0.5, 1), uniform(0.5, 1))
            touch.ud['line'] = Line (points = (touch.x, touch.y), width = t)
    def on_touch_move(self, touch):
        touch.ud['line']. points += [touch.x, touch.y]

class MyPaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        parent.add_widget(self.painter)

        clearbtn = Button(text = 'Очистить', size = (75, 50), on_press = self.clear_canvas)
        colorbtn = Button(text = 'Цвет', size = (75, 50), on_press = self.change_color )
        colorbtn.pos = 80,0
        global t
        plusbtn = Button(text = '+', size = (75, 50), on_press = self.plus_canvas)
        plusbtn.pos = 0,100
        minusbtn = Button(text = '-', size = (75, 50), on_press = self.minus_color)
        minusbtn.pos = 80,100
        parent.add_widget(clearbtn)
        parent.add_widget(colorbtn)
        parent.add_widget(minusbtn)
        parent.add_widget(plusbtn)

        return parent


    def clear_canvas(self, obj):
        self.painter.canvas.clear()

    def change_color(self, obj):
        clr_picker = ColorPicker()
    def plus_canvas(self, obj):
        global t
        t+=1
        

    def minus_color(self, obj):
        global t
        if(t>1):
            t-=1

if __name__=='__main__':
    MyPaintApp().run()