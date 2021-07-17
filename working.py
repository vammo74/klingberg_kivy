from random import choice
import kivy

from kivy.app import App
from kivy.core.window import Window

from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty
from kivy.properties import StringProperty
from kivy.properties import DictProperty
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty

from kivy.animation import Animation

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton

from kivy.clock import Clock

kivy.require('1.11.0')

class Meter(FloatLayout):
    pass


class Table(GridLayout):
    """Class for drawing and modifying
    the multiplication table layout and widgets"""

    button_memory_hor = ListProperty([])
    button_memory_vert = ListProperty([])

    btn = ObjectProperty()
    _id = StringProperty()
    content = ListProperty()
    colour = ListProperty()

    def __init__(self, **kwargs):
        super(Table, self).__init__(**kwargs)
        self.draw_table(self)
        self.cols = 10
        self.rows = 10


    def draw_table(self, *args):
        app = App.get_running_app()
        self.colour = (0, 0, 0, 0)

        for i in range(100):
            if i in [i for i in range(91, 100)]:
                self._id = "tab"+str(i)
                self.btn = ToggleButton(
                    text="",
                    background_color=self.colour,
                    background_normal='table_tog_up.png',
                    background_down='table_tog_down.png',
                    disabled=True,
                    group='horizontal',
                    on_press=self._change_colour_hor
                )
                app.table_ids[self._id] = self.btn
                self.add_widget(self.btn)
            elif i in [i for i in range(0, 81, 10)]:
                self._id = "tab"+str(i)
                self.btn = ToggleButton(
                    text="",
                    background_color=self.colour,
                    background_normal='table_tog_up.png',
                    background_down='table_tog_down.png',
                    disabled=True,
                    group='vertical',
                    on_press=self._change_colour_vert
                )
                app.table_ids[self._id] = self.btn
                self.add_widget(self.btn)
            elif i == 90:
                self._id = "tab"+str(i)
                self.btn = Button(
                    text="",
                    background_color=self.colour,
                    background_normal='table_tog_up.png',
                    background_down='table_tog_up.png',
                    disabled=True
                )
                app.table_ids[self._id] = self.btn
                self.add_widget(self.btn)
            else:
                self._id = "tab"+str(i)
                self.btn = Button(
                    text="",
                    background_color=self.colour,
                    background_normal='table3.png',
                    background_down='table3.png',
                    disabled=True
                )
                app.table_ids[self._id] = self.btn
                self.add_widget(self.btn)


    def _change_colour_hor(self, instance, *largs):
        app = App.get_running_app()
        if instance.state == 'down':
            self._clear_colour_hor()
            target = int(instance.text)
            x = target
            for i in range(x - 1, x + 81, 10):
                self.button_memory_hor.append(i)
                target_button = app.table_ids['tab'+str(i)]
                target_button.background_color = (.5, .5, 1, 1)
            for i in self.button_memory_hor:
                if i in self.button_memory_vert:
                    target_button = app.table_ids['tab'+str(i)]
                    target_button.background_color = (0, 0, 1, 1)
        if instance.state != 'down':
            self._clear_colour_hor()

    def _clear_colour_hor(self):
        app = App.get_running_app()
        for i in self.button_memory_hor:
            if i and i not in self.button_memory_vert:
                target_button = app.table_ids['tab'+str(i)]
                target_button.background_color = (1, 1, 1, 1)
            if i and i in self.button_memory_vert:
                target_button = app.table_ids['tab'+str(i)]
                if target_button.background_color == (.5, .5, 1, 1):
                    target_button.background_color = (1, 1, 1, 1)
                else:
                    target_button.background_color = (.5, .5, 1, 1)
        self.button_memory_hor = []

    def _change_colour_vert(self, instance, *largs):
        app = App.get_running_app()
        if instance.state == 'down':
            self._clear_colour_vert()
            target = int(instance.text)
            x = 100-target*10
            for i in range(x + 1, x + 10):
                self.button_memory_vert.append(i)
                target_button = app.table_ids['tab'+str(i)]
                target_button.background_color = (.5, .5, 1, 1)
            for i in self.button_memory_vert:
                if i in self.button_memory_hor:
                    target_button = app.table_ids['tab'+str(i)]
                    target_button.background_color = (0, 0, 1, 1)
        if instance.state != 'down':
            self._clear_colour_vert()

    def _clear_colour_vert(self):
        app = App.get_running_app()
        for i in self.button_memory_vert:
            if i and i not in self.button_memory_hor:
                target_button = app.table_ids['tab'+str(i)]
                target_button.background_color = (1, 1, 1, 1)
            if i and i in self.button_memory_hor:
                target_button = app.table_ids['tab'+str(i)]
                if target_button.background_color == (.5, .5, 1, 1):
                    target_button.background_color = (1, 1, 1, 1)
                else:
                    target_button.background_color = (.5, .5, 1, 1)
            self.button_memory_vert = []

    def table_off(self, *largs):
        app = App.get_running_app()
        for i in range(100):
            target_button = app.table_ids['tab'+str(i)]
            target_button.background_color = (0, 0, 0, 0)
            target_button.disabled = True
            target_button.text = ""

    def table_on(self, *args):
        app = App.get_running_app()
        self.content = []
        for i in range(10, 0, -1):
            for n in range(1, 11):
                number = i*n
                self.content.append(str(number))
        for i in range(1, app.level):
            for n in range(1, app.level):
                index = (9 - i)*10 + n
                self.content[index] = ''
        for i in range(100):
            if i in [i for i in range(90, 100)]:
                target_button = app.table_ids['tab'+str(i)]
                target_button.background_color = (.8, .8, .8, 1)
                target_button.disabled = False
                target_button.text = self.content[i]
            elif i in [i for i in range(0, 81, 10)]:
                target_button = app.table_ids['tab'+str(i)]
                target_button.background_color = (.8, .8, .8, 1)
                target_button.disabled = False
                target_button.text = self.content[i]
            else:
                target_button = app.table_ids['tab'+str(i)]
                target_button.background_color = (1, 1, 1, 1)
                target_button.disabled = False
                target_button.text = self.content[i]


class Display(BoxLayout):

    disp_ids = DictProperty({})

    def __init__(self, **kwargs):
        super(Display, self).__init__(**kwargs)
        Clock.schedule_once(self._get_disp_ids)

    def _get_disp_ids(self, *args):
        app = App.get_running_app()
        for namn, objekt in enumerate(self.children):
            _id = "dbtn" + str(namn)
            app.disp_ids[_id] = objekt


class Keypad(GridLayout):
    pass



class MyButton(Button):

    def _on_press(self, instance, *largs):
        app = App.get_running_app()
        if app.disp_ids['dbtn0'].state == 'down':
            if instance.text == 'Enter':
                self._on_enter()
 

            elif instance.text == 'Del':
                if app.result:
                    app.result = app.result[:-1]
                    app.disp_ids['dbtn1'].text = app.result
            else:
                if len(app.result) < 3:
                    app.result += str(instance.text)
                    app.disp_ids['dbtn1'].text = app.result
                    
    def _on_enter(self, *args):
        app = App.get_running_app()
        if app.disp_ids['dbtn1'].text == str(app.integer_answer()):
            app.root.flash_green()
            if app.level == 0:
                app.stop_timer()
                app.test_analysis[app.disp_ids['dbtn2'].text] = app.speed
                app.start_timer()
                if len(app.product_list) == 0:
                    self.analyse()
                    app.product_list = app.generate_products()
                    app.stop_timer()
                    app.level = app.generate_level()
                    app.table.table_on()
                else:
                    app.product = choice(app.product_list)
                    app.product_list.remove(app.product)
                    app.disp_ids['dbtn2'].text = app.product
                    app.result = ''
                    app.disp_ids['dbtn1'].text = ''
            else:
                if len(app.product_list) == 0:
                    app.level += 1
                    app.level_up = True
                    app.disp_ids['dbtn0'].state = 'normal'
                    app.stop_timer()
                    app.disp_ids['dbtn0'].text = 'Start'
                    app.disp_ids['dbtn0'].background_normal = 'new_level.png'
                    app.disp_ids['dbtn1'].text = ''
                    app.disp_ids['dbtn2'].text = ''
                    app.disp_ids['dbtn1'].disabled = True
                    app.disp_ids['dbtn2'].disabled = True
                    app.product_list = app.generate_products()
                    app.table.table_off(app.table)
                    app.root.save_state()
                else:
                    app.product = choice(app.product_list)
                    app.product_list.remove(app.product)
                    app.disp_ids['dbtn2'].text = app.product
                    app.result = ''
                    app.disp_ids['dbtn1'].text = ''
                    if app.level > 8:
                    	app.stop_timer()
                    	app.start_timer()
        else:
            app.root.flash_red()
            if app.level == 0:
                app.factors.append(app.product[0])
                app.factors.append(app.product[-1])
                app.test_analysis[app.disp_ids['dbtn2'].text] = 'wrong'
                if len(app.product_list) == 0:
                    self.analyse()
                    app.product_list = app.generate_products()
                    app.stop_timer()
                    app.level = app.generate_level()
                    print('level', app.level)
                    app.table.table_on()
                app.product = choice(app.product_list)
                app.product_list.remove(app.product)
                app.disp_ids['dbtn2'].text = app.product
                app.result = ''
                app.disp_ids['dbtn1'].text = ''
                app.stop_timer()
                app.start_timer()
            if app.level > 0:
                app.product_list.append(app.product)
                app.result = ''
                app.disp_ids['dbtn1'].text = ''
                if len(app.product_list) > 49:
                    app.level -= 1
                    if app.level == 0: app.level = 1
                    app.level_down = True
                    app.disp_ids['dbtn0'].state = 'normal'
                    app.stop_timer()
                    app.disp_ids['dbtn0'].text = 'Start'
                    app.disp_ids['dbtn0'].background_normal = 'level_down.png'
                    app.disp_ids['dbtn1'].text = ''
                    app.disp_ids['dbtn2'].text = ''
                    app.disp_ids['dbtn1'].disabled = True
                    app.disp_ids['dbtn2'].disabled = True
                    app.product_list = app.generate_products()
                    app.table.table_off(app.table)
                    app.root.save_state()
                if app.level > 8:
                    app.table.table_off()
                    app.stop_timer()
                    app.start_timer()

    def analyse(self, *largs):
        app = App.get_running_app()
        analysis = ""
        times_orders = sorted(app.test_analysis.items(), key=lambda x: x[0], reverse=False)
        for key, time in times_orders:
            if isinstance(time, int):
                string = "You answered " + key + " correctly in " + str(20*time//360) + " seconds\n"
                analysis += string
            if isinstance(time, str):
                if time == "wrong":
                    analysis += "You gave the wrong answer to " + key + " \n"
                if time == "timed out":
                    analysis += "You timed out with " + key + " \n"
        print(analysis)
        ana = open('klingberg.analysis', 'w')
        ana.write(analysis)
        ana.close()





class Klingberg(RelativeLayout):
    #Window.size = (1200, 650)
    button = ObjectProperty()

    def __init__(self, **kwargs):
        super(Klingberg, self).__init__(**kwargs)
        Clock.schedule_once(self._get_klingberg_ids)

    def _get_klingberg_ids(self, *args):
        app = App.get_running_app()
        for namn, objekt in enumerate(self.children):
            _id = "kbtn" + str(namn)
            app.root_ids[_id] = objekt
        Clock.schedule_once(self._get_timer_ids)

    def _get_timer_ids(self, *args):
        app = App.get_running_app()
        for namn, objekt in enumerate(app.root_ids['kbtn4'].children):
            _id = "tbtn" + str(namn)
            app.timer_ids[_id] = objekt


    def _start(self, *args):
        app = App.get_running_app()

        if app.disp_ids['dbtn0'].state == 'down':
            app.disp_ids['dbtn1'].disabled = False
            app.disp_ids['dbtn2'].disabled = False
            app.root.load_state()
            app.product = choice(app.product_list)
            app.product_list.remove(app.product)
            app.disp_ids['dbtn2'].text = app.product
            app.disp_ids['dbtn0'].text = 'Save'
            app.result = ''
            if app.level == 0:
                app.start_timer()
            elif app.level > 8:
                app.stop_timer()
                app.table.table_off()
                app.start_timer()
            else:
                app.table.table_on(app.table)
        else:
            if app.level_down: print('starting down')
            app.stop_timer()
            print(app.tid)
            app.disp_ids['dbtn0'].background_normal = 'start.png'
            app.disp_ids['dbtn0'].text = 'Start'
            app.disp_ids['dbtn1'].text = ''
            app.disp_ids['dbtn2'].text = ''
            app.disp_ids['dbtn1'].disabled = True
            app.disp_ids['dbtn2'].disabled = True
            app.table.table_off(app.table)
            app.product_list.append(app.product)
            app.root.save_state()

    def load_state(self, *args):
        app = App.get_running_app()
        try:
            fob = open("klingberg.save", "r+")
            state = fob.read().split(";")
            levels = state[0].split(',')
            app.level = int(levels[0])
            app.counter = int(levels[1])
            app.product_list = state[1].split(',')
            app.factors = state[2].split(',')
            fob.close()
        except FileNotFoundError:
            app.level = 0
            app.counter = 0
        if app.product_list == ['']:
            app.product_list = app.generate_products()
        if app.factors == ['']:
            app.factors = []

    def flash_red(self, *args):
        app = App.get_running_app()
        app.disp_ids['dbtn1'].background_color = (.95, .2, 0, 1)
        def reset_colour(*args):
            app.disp_ids['dbtn1'].background_color = 1, 1, 1, 1
        Clock.schedule_once(reset_colour, .25)

    def flash_green(self, *args):
        app = App.get_running_app()
        app.disp_ids['dbtn1'].background_color = (0, 1, 0, 1)
        def reset_colour(*args):
            app.disp_ids['dbtn1'].background_color = 1, 1, 1, 1
        Clock.schedule_once(reset_colour, .25)


    def save_state(self, *args):
        app = App.get_running_app()
        fob = open('klingberg.save', 'w')
        fob.write(str(app.level) + "," + str(app.counter))
        fob.write(";")
        for i in app.product_list[ : -1]:
            fob.write(i + ",")
        fob.write(app.product_list[-1] + ";")
        if app.factors:
            if len(app.factors) >= 2:
                for i in app.factors[ : -1]:
                    fob.write(i + ",")
            fob.write(app.factors[-1])
        fob.close()



class KlingbergApp(App):
    a = NumericProperty(0)
    b = NumericProperty(0)

    product = StringProperty('')
    answer = NumericProperty()
    int_answer = NumericProperty(0)
    tid = NumericProperty(20)
    level = NumericProperty(0)
    counter = NumericProperty(0)
    speed = NumericProperty(0)
    product = StringProperty('')
    result = StringProperty('')

    table = ObjectProperty()
    display = ObjectProperty()
    keypad = ObjectProperty()
    meter = ObjectProperty()
    my_button = ObjectProperty()
    target = ObjectProperty()
    button = ObjectProperty()

    level_up = BooleanProperty(False)
    level_down = BooleanProperty(False)

    product_list = ListProperty([''])
    add_on_products = ListProperty([])
    factors = ListProperty([''])

    disp_ids = DictProperty({})
    table_ids = DictProperty({})
    meter_ids = DictProperty({})
    root_ids = DictProperty({})
    timer_ids = DictProperty({})
    test_analysis = DictProperty({})

    root = Klingberg()

    def __init__(self, **kwargs):
        super(KlingbergApp, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._on_keyboard)


    def _on_keyboard(self, keyboard, key, scancode, codepoint, modifier):
        if codepoint in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            self.button = Button(text=codepoint)
            self.my_button._on_press(self.button)
        if key == 127 or key == 8:
            self.button = Button(text='Del')
            self.my_button._on_press(self.button)
        if key == 13:
            self.button = Button(text='Enter')
            self.my_button._on_press(self.button)

    def generate_products(self, *args):
        productList = []
        for a in range(2, 11):
            for b in range(2, 10):
                if str(a)+" × "+str(b) not in productList and str(b)+" × "+str(a) not in productList:
                    productList.append(str(a)+" × "+str(b))
        productList = productList + self.add_on_products
        return productList

    def generate_level(self, *args):
        wrong = {}
        for i in range(2, 10):
            wrong["x"+str(i)] = self.factors.count(str(i))
        if wrong['x2'] >= 8: return 1
        elif wrong['x3'] >= 7:
            return 2
        elif wrong['x4'] >= 6:
            return 3
        elif wrong['x5'] >= 5:
            return 4
        elif wrong['x6'] >= 4:
            return 5
        elif wrong['x7'] >= 3:
            return 6
        elif wrong['x8'] >= 2:
            return 7
        elif wrong['x9'] >= 2:
            return 8
        else:
            return 9

    def integer_answer(self, *args):
        str_answer = self.product.split(" × ")
        self.answer = int(str_answer[0])*int(str_answer[1])
        return self.answer

    def start_timer(self, *args):
        app = App.get_running_app()
        anim = Animation(angle=360, duration=(self.tid-self.level))
        anim.start(self.timer_ids['tbtn0'])
        anim.bind(on_complete=lambda self, x: app._too_slow())


    def stop_timer(self, *args):
        Animation.cancel_all(self.timer_ids['tbtn0'])
        n = self.timer_ids['tbtn0'].angle
        self.speed = int(n)
        self.timer_ids['tbtn0'].angle = 0

    def _too_slow(self, *args):
        if self.level == 0:
            self.test_analysis[self.disp_ids['dbtn2'].text] = "timed out"
            if len(self.product_list) == 0:
                self.my_button.analyse()
                self.product_list = self.generate_products()
                self.stop_timer()
                self.level = self.generate_level()
                self.disp_ids['dbtn0'].text = 'Start'
                self.disp_ids['dbtn0'].state = 'normal'
                self.disp_ids['dbtn0'].background_normal = 'new_level.png'
                self.disp_ids['dbtn1'].text = ''
                self.disp_ids['dbtn2'].text = ''
                self.disp_ids['dbtn1'].disabled = True
                self.disp_ids['dbtn2'].disabled = True
                self.product_list = self.generate_products()
                self.table.table_off(self.table)
                self.root.save_state()
            else:

                self.product = choice(self.product_list)
                self.product_list.remove(self.product)
                self.disp_ids['dbtn2'].text = self.product
                self.result = ''
                self.disp_ids['dbtn1'].text = ''
                self.timer_ids['tbtn0'].angle = 0
                self.start_timer()
        else:
            self.product_list.append(self.product)
            self.product_list.append(self.product)
            if len(self.product_list) > 49:
                self.level -= 1
                if self.level == 0: self.level = 1
                self.product_list = self.generate_products()
                self.disp_ids['dbtn0'].text = 'Start'
                self.disp_ids['dbtn0'].state = 'normal'
                self.disp_ids['dbtn0'].background_normal = 'level_down.png'
                self.disp_ids['dbtn1'].text = ''
                self.disp_ids['dbtn2'].text = ''
                self.disp_ids['dbtn1'].disabled = True
                self.disp_ids['dbtn2'].disabled = True
                self.root.save_state()
            else:
                self.product = choice(self.product_list)
                self.product_list.remove(self.product)
                self.disp_ids['dbtn2'].text = self.product
                self.result = ''
                self.disp_ids['dbtn1'].text = ''
                self.timer_ids['tbtn0'].angle = 0
                self.start_timer()



    def build(self):
        self.table = Table()
        self.display = Display()
        self.keypad = Keypad()
        self.my_button = MyButton()
        self.meter = Meter()
        return Klingberg()

if __name__ == '__main__':
    KlingbergApp().run()
