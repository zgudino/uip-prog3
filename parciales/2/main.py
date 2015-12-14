from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
import requests, json


class MyDrop(App):
    def __init__(self, **kwargs):
        super(MyDrop, self).__init__(**kwargs)

        api = 'http://127.0.0.1:3000/api/1.0/places.json'
        resp = requests.get(api)
        places = []

        try:
            if not resp.status_code == 200:
                raise Exception('ApiException', 'Error found while calling the API backend')

            for data in [resp.json()[key] for key in resp.json().keys() if key == 'data']:
                for place in data:
                    places.append(place['name'])

            self.lista = tuple(places)
        except Exception as err:
            return err

    def d(self, n):
        self.dropdown.select(n.text)

    def build(self):
        self.box = FloatLayout()
        self.l = Label(pos_hint={'x': 0.5 / 2, 'center_y': 0.9},
                       size_hint=(0.5, 0.2),
                       text='[color=ff3333][b][size=35]TARIFAS DE TAXI[/b][/color]',
                       markup=True)
        self.dropdown = DropDown()

        for i in self.lista:
            b1 = Button(text=i, size_hint_y=None, height=50)
            b1.bind(on_release=self.d)
            self.dropdown.add_widget(b1)

        self.b2 = Button(pos_hint={'x': 0, 'center_y': .4},
                         size_hint=(0.5, 0.2),
                         text='[color=3333ff][size=24]ORIGEN[/color]',
                         markup=True)
        self.b2.bind(on_release=self.dropdown.open)
        self.b3 = Button(pos_hint={'x': 0.5, 'center_y': .4}, size_hint=(0.5, 0.2),
                         text='[color=3333ff][size=24]DESTINO[/color]', markup=True)
        self.b3.bind(on_release=self.dropdown.open)
        self.b_calcular = Button(pos_hint={'x': 0.5 / 2, 'center_y': .1}, size_hint=(0.5, 0.2),
                                 text='[color=3333ff][size=24]CALCULAR TARIFA[/color]', markup=True)
        self.b_calcular.bind()
        self.box.add_widget(self.b2)
        self.box.add_widget(self.b3)
        self.box.add_widget(self.b_calcular)
        self.box.add_widget(self.l)
        return self.box

if __name__ == "__main__":
    MyDrop().run()
