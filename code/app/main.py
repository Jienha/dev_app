from kivy.app import App
from kivy.uix.widget import Widget

# Create Game Widget
class PongGame(Widget):
    pass

# create App that calls the Game Widget: 
class PongApp(App):
    def build(self):
        return PongGame()
    
if __name__ == '__main__':
    PongApp().run()