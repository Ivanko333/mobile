from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.properties import BooleanProperty
import instr
from ruffier import test


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        text = Label(text=instr.txt_instruction)
        layout1 = BoxLayout(padding=8, spacing=8, orientation='vertical')
        layout2 = BoxLayout(size_hint=(.5, None), pos_hint={'center_x': 0.5, 'center_y': 0.5}, height="30sp")
        layout3 = BoxLayout(size_hint=(.5, None), pos_hint={'center_x': 0.5, 'center_y': 0.5}, height="30sp")
        input1 = TextInput(hint_text="Введите имя")
        self.input2 = TextInput(hint_text="Введите Ваш возраст")
        layout1.add_widget(text)
        layout2.add_widget(input1)
        layout3.add_widget(self.input2)
        layout1.add_widget(layout2)
        layout1.add_widget(layout3)
        button = Button(text='Далее!!!', size_hint=(.3, .3),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button.on_press = self.next
        layout1.add_widget(button)
        self.add_widget(layout1)

    def next(self):
        age = check_int(self.input2.text)
        if not age or age < 7:
            self.input2.text = "Ошибка! Введите целое число от 7!"

        else:
            self.manager.current = 'second'


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        text = Label(text=instr.txt_test1)
        text1 = Label(text="Введите результат:")
        self.input1 = TextInput()
        self.input1.set_disabled(True)
        layout = BoxLayout(padding=10, spacing=10, orientation='vertical')
        layout1 = BoxLayout(orientation='horizontal', size_hint=(1, None), height="30sp")
        self.timer = Time(15)
        self.timer.bind(done=self.handler)
        self.next_screen = False
        layout.add_widget(text)
        layout1.add_widget(text1)
        layout1.add_widget(self.input1)
        layout.add_widget(layout1)
        layout1.add_widget(self.timer)
        self.button = Button(text='Запустить таймер', size_hint=(.5, .2),
                             pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.button.on_press = self.next
        layout.add_widget(self.button)
        self.add_widget(layout)

    def next(self):
        if self.next_screen:
            result = check_int(self.input1.text)
            if not result:
                self.input1.text = "Ошибка! Введите целое число!"

            else:
                self.manager.current = 'third'
        else:
            self.button.set_disabled(True)
            self.timer.start()

    def handler(self, *args):
        self.next_screen = True
        self.button.set_disabled(False)
        self.button.text = "Далее"
        self.input1.set_disabled(False)


class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        text = Label(text=instr.txt_test2)
        layout1 = BoxLayout(padding=8, spacing=8, orientation='vertical')
        layout1.add_widget(text)
        button = ScreenButton(self, text='Далее!!!', direction='left', goal='four', size_hint=(.3, .2),
                              pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout1.add_widget(button)
        self.add_widget(layout1)


class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        text = Label(text=instr.txt_test3)
        text1 = Label(text="Результате:")
        text2 = Label(text="Результате после отдыха:")
        self.input1 = TextInput(hint_text="0")
        self.input2 = TextInput(hint_text="0")
        layout1 = BoxLayout(padding=8, spacing=8, orientation='vertical')
        layout2 = BoxLayout(orientation="horizontal", size_hint=(1, None), height="30sp")
        layout3 = BoxLayout(orientation="horizontal", size_hint=(1, None), height="30sp")
        self.timer = Time(15)
        self.timer.bind(done=self.handler)
        self.stager = 0
        self.input1.set_disabled(True)
        self.input2.set_disabled(True)
        layout1.add_widget(text)
        layout1.add_widget(self.timer)
        layout2.add_widget(text1)
        layout2.add_widget(self.input1)
        layout3.add_widget(text2)
        layout3.add_widget(self.input2)
        layout1.add_widget(layout2)
        layout1.add_widget(layout3)
        self.next_screen = False
        self.button = Button(text='Запустить таймер', size_hint=(.3, .2),
                             pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout1.add_widget(self.button)
        self.button.on_press = self.next
        self.add_widget(layout1)

    def next(self):
        if self.next_screen:
            result1 = check_int(self.input1.text)
            result2 = check_int(self.input2.text)
            if not result1:
                self.input1.text = "Ошибка! Введите целое число!"
            else:
                if not result2:
                    self.input2.text = "Ошибка! Введите целое число!"
                else:
                    self.manager.current = 'result'

        else:
            self.button.set_disabled(True)
            self.timer.start()

    def handler(self, *args):
        if self.timer.done:
            if self.stager == 0:
                self.stager += 1
                self.timer.restart(30)
                self.input1.set_disabled(False)
                self.button.text = "Отдыхайте"
            elif self.stager == 1:
                self.stager += 1
                self.timer.restart(15)
                self.button.text = "Посчитайте свой пульс"
            elif self.stager == 2:
                self.input2.set_disabled(False)
                self.button.set_disabled(False)
                self.button.text = "Далее"
                self.next_screen = True


class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.instr = Label(text='')
        self.outer.add_widget(self.instr)
        self.add_widget(self.outer)
        self.on_enter = self.before

    def before(self):
        global name
        self.instr.text = name + '\n' + test(p1, p2, p3, age)


class Time(Label):
    done = BooleanProperty(False)

    def __init__(self, time, **kwargs):
        self.done = False
        self.time = time
        self.current = 0
        my_text = f"Прошло секунд: {self.current}"
        super().__init__(text=my_text, **kwargs)

    def restart(self, total, **kwargs):
        self.done = False
        self.time = total
        self.current = 0
        self.text = f"Прошло секунд: {self.current}"
        self.start()

    def start(self):
        Clock.schedule_interval(self.change, 1)

    def change(self, t):
        self.current += 1
        self.text = f"Прошло секунд: {self.current}"
        if self.current >= self.time:
            self.done = True
            return False


class ScreenButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal


def check_int(number):
    try:
        number = int(number)
        return number
    except Exception as err:
        print(err)
        return False


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name="main"))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name="third"))
        sm.add_widget(FourthScreen(name="four"))
        sm.add_widget(Result(name="result"))
        return sm


application = MyApp()
application.run()
