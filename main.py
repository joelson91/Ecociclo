from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.utils import get_color_from_hex
from screens.login import LoginScreen
from screens.home import HomeScreen
from screens.learn import LearnScreen, ContentScreen
from kivy.core.text import LabelBase

# Registar a fonte com um nome identificador (ex: 'MinhaFonte')
LabelBase.register(
    name='headline_font',
    fn_regular='media/fonts/Fraunces_72pt-Regular.ttf',  # Caminho para a fonte normal
    fn_bold='media/fonts/Fraunces_72pt-Bold.ttf'  # Caminho para a versão negrito (opcional)
)

LabelBase.register(
    name='body_font',
    fn_regular='media/fonts/PlusJakartaSans-Regular.ttf',  # Caminho para a fonte normal
    fn_bold='media/fonts/PlusJakartaSans-Bold.ttf'  # Caminho para a versão negrito (opcional)
)

Window.clearcolor = get_color_from_hex("fbfcfb")
Builder.load_file("kv/styles.kv")


class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="Login"))
        sm.add_widget(HomeScreen(name="Home"))
        sm.add_widget(LearnScreen(name="Learn"))
        sm.add_widget(ContentScreen(name="Content"))
        return sm


if __name__ == '__main__':
    MainApp().run()
