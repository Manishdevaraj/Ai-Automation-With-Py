import kivy
from kivy.app import App
from kivy.uix.button import Label

class hello(App):
    def build(self):
        
        return Label(text="hello",font_size="50sp")
    
k=hello()
k.run()
