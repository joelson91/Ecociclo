from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.utils import get_color_from_hex
from screens.login import LoginScreen
from screens.home import HomeScreen
from screens.learn import LearnScreen, ContentScreen
from screens.goals import GoalScreen
from screens.news import NewsScreen
from screens.about import AboutScreen
from kivy.core.text import LabelBase

LabelBase.register(
    name='headline_font',
    fn_regular='media/fonts/Fraunces_72pt-Regular.ttf',
    fn_bold='media/fonts/Fraunces_72pt-Bold.ttf'
)

LabelBase.register(
    name='body_font',
    fn_regular='media/fonts/PlusJakartaSans-Regular.ttf',
    fn_bold='media/fonts/PlusJakartaSans-Bold.ttf'
)

Window.clearcolor = get_color_from_hex("fbfcfb")
Builder.load_file("kv/styles.kv")


class MainApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(LoginScreen(name="Login"))
        self.sm.add_widget(HomeScreen(name="Home"))
        self.sm.add_widget(LearnScreen(name="Learn"))
        self.sm.add_widget(ContentScreen(name="Content"))
        self.sm.add_widget(GoalScreen(name="Goal"))
        self.sm.add_widget(NewsScreen(name="News"))
        self.sm.add_widget(AboutScreen(name="About"))

        Window.bind(on_keyboard=self.controlar_botao_voltar)
        return self.sm

    def controlar_botao_voltar(self, window, key, scancode, codepoint, modifier):
        if key == 27:
            return self.processar_retorno_de_tela()
        return False

    def processar_retorno_de_tela(self):
        tela_atual = self.sm.current

        if tela_atual == "Home" or tela_atual == "Login":
            return False

        elif tela_atual == "Content":
            self.sm.transition.direction = "right"
            self.sm.current = "Learn"
            return True

        else:
            self.sm.transition.direction = "right"
            self.sm.current = "Home"
            return True


if __name__ == '__main__':
    MainApp().run()
