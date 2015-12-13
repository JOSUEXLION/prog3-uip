import json
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import NumericProperty, StringProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.core.window import Window


Window.clearcolor = (1, 1, 1, 1)


class TaxiCosto(Screen):

    _layaout = ObjectProperty(None)
    _drop_a = ObjectProperty(None)
    _drop_b = ObjectProperty(None)
    price = StringProperty('0.00')

    def alertNotification(self, title, text):
        popup = Popup(title=title, content=Label(text=text), size_hint=(None, None), size=(400, 300))
        popup.open()

    def getCosto(self):

        if(self._drop_a.text != 'Origen' and self._drop_b.text != 'Destino'):
            opt_a = self.ubicationsData[self._drop_a.text]
            opt_b = self.ubicationsData[self._drop_b.text]
            if opt_a in self.prices[opt_b]:
                self.price = 'B/. ' + self.prices[opt_b][opt_a]
            else:
                self.price = 'Incalculable! :('
        else:
            self.alertNotification('Campos incompletos', 'Por favor. \nllene las opciones!.')

    def onSelectDropDown(self, drop):
        self.selectDrop = drop

    """docstring for TaxiCosto"""
    def __init__(self, *args, **kwargs):
        super(TaxiCosto, self).__init__(*args, **kwargs)

        # read json config ubications
        with open('ubications.json') as ubi_file:
            self.ubications = json.load(ubi_file)

        with open('prices.json') as pri_file:
            self.prices = json.load(pri_file)

        self.ubicationsData = {}
        # create dropdownList
        dropdown = DropDown()
        for ubication in self.ubications:
            self.ubicationsData[ubication['name']] = ubication['type']
            # when adding widgets, we need to specify the height manually (disabling
            # the size_hint_y) so the dropdown can calculate the area it needs.
            btn = Button(text=ubication['name'], size_hint_y=None, height=60)
            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            btn.bind(on_release=lambda btn: dropdown.select(btn))

            # then add the button inside the dropdown
            dropdown.add_widget(btn)

        self._drop_a.bind(on_release=dropdown.open)
        self._drop_b.bind(on_release=dropdown.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        dropdown.bind(on_select=lambda instance, x: instanceDrop(x))
        # self._layaout.add_widget(self._drop_a)

        def instanceDrop(a):
            self.price = '0.00'
            if(self.selectDrop == 'a'):
                self._drop_a.text = a.text
            else:
                self._drop_b.text = a.text

class MainApp(App):
    def build(self):
        taxi = TaxiCosto()
        return taxi


if __name__ == '__main__':
    MainApp().run()

__version__ = "0.0.1"
