from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('kv/account.kv')


class AccountScreen(Screen):
    pass


class LoginScreen(Screen):
    def fazer_login(self):
        pass


class RegisterScreen(Screen):
    def fazer_cadastro(self):
        pass
