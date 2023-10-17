from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
import instr


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        text = Label(text=instr.txt_instruction)
        layout1 = BoxLayout(padding=8, spacing=8, orientation='vertical')
        layout2 = BoxLayout(size_hint=(.5, None), pos_hint={'center_x': 0.5, 'center_y': 0.5}, height="30sp")
        layout3 = BoxLayout(size_hint=(.5, None), pos_hint={'center_x': 0.5, 'center_y': 0.5}, height="30sp")
        input1 = TextInput(hint_text=instr.txt_name)
        input2 = TextInput(hint_text="Введите Ваш возраст")
        layout1.add_widget(text)
        layout2.add_widget(input1)
        layout3.add_widget(input2)
        layout1.add_widget(layout2)
        layout1.add_widget(layout3)
        button = ScreenButton(self, text='Далее!!!', direction='left', goal='second', size_hint=(.3, .3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout1.add_widget(button)
        self.add_widget(layout1)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name="main"))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name="third"))
        sm.add_widget(FourthScreen(name="four"))
        return sm


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        text = Label(text=instr.txt_test1)
        text1 = Label(text="Введите результат:")
        input1 = TextInput()
        layout = BoxLayout(padding=10, spacing=10, orientation='vertical')
        layout1 = BoxLayout(orientation='horizontal', size_hint=(1, None), height="30sp")
        layout.add_widget(text)
        layout1.add_widget(text1)
        layout1.add_widget(input1)
        layout.add_widget(layout1)
        button = ScreenButton(self, text='Далее', direction='left', goal='third', size_hint=(.5, .2), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(button)
        self.add_widget(layout)


class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        text = Label(text=instr.txt_test3)
        text1 = Label(text="Результат:")
        text2 = Label(text='Результат после отдыха:')
        input1 = TextInput(hint_text='0')
        input2 = TextInput(hint_text='0')
        layout1 = BoxLayout(padding=8, spacing=8, orientation='vertical')
        layout1.add_widget(text)
        button = ScreenButton(self, text='Далее!!!', direction='left', goal='four', size_hint=(.3, .2), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout1.add_widget(button)
        self.add_widget(layout1)


class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        text = Label(text=instr.txt_test2)
        layout1 = BoxLayout(padding=8, spacing=8, orientation='vertical')
        layout1.add_widget(text)
        button = ScreenButton(self, text='Далее!!!', direction='left', goal='main', size_hint=(.3, .2), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout1.add_widget(button)
        self.add_widget(layout1)


class ScreenButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal


application = MyApp()
application.run()
