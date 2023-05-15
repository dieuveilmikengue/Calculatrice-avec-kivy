from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kaki.app import App
from kivy.factory import Factory
from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout

class Calculatrice(BoxLayout):
    def calculer(self, reponse):
        if reponse:
            try:
                self.retour.text = str(eval(reponse))
            except Exception:
                self.retour.text = "Erreur"

    def reinit(self, expression):
        if expression:
            self.display.text = ''
            self.retour.text = ''


class calculatriceApp(App):

    DEBUG = 1

    KV_FILES = {
        os.path.join(os.getcwd(), "calculatrice.kv"),
    }
    CLASSES = {
        "Calculatrice": "calculatrice",
    }
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
        ]


    def build(self):
        self.title = "Calculatrice"


    
Config.set("graphics", "width", "250")
Config.set("graphics", "height", "415")

if __name__ == "__main__":
    calculatriceApp().run()