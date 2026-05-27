from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from screens.account import AccountScreen, LoginScreen, RegisterScreen
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex("f0e8d8")
Builder.load_file("kv/styles.kv")


class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(AccountScreen(name="Account"))
        sm.add_widget(LoginScreen(name="Login"))
        sm.add_widget(RegisterScreen(name="Register"))
        return sm


if __name__ == '__main__':
    MainApp().run()
