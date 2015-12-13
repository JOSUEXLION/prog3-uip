#josue de leon
# Tarea 7
#8-876-2357
'''1.Crear una aplicacion en Kivy que maneje un registro de asistencia. Basicamente la aplicacion debe contener una 
 etiqueta que diga "Nombre: ", un campo para ingresar cadenas de texto, un boton que diga "Guardar" y otro botin 
 que diga "Exportar". El botn para guardar agrega el contenido del campo a una lista de asistencia. El boton para 
exportar salva la lista de asistencia a un fichero con extension TXT'''


import listasutils as lu
from kivy.app import App 
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty



Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

class Fondo(FloatLayout):
    lista = []
    listgrid = ObjectProperty(None)
    textbox = ObjectProperty(None)

    def OnGuardarClick(self,texto):

        if texto != "":
            grid = self.listgrid
            grid.bind(minimum_height=grid.setter('height'), minimum_width=grid.setter('width'))

            self.textbox.text = ''
            self.lista.append(texto)

            RowNombre = Label(text='{0}'.format(texto))
            grid.add_widget(RowNombre)

    def OnExportarClick(self):
        lu.salvarLista("Tarea7.txt",self.lista)

class AsistenciaApp(App):
    def build(self):
        return Fondo()

if __name__ == '__main__': 
    AsistenciaApp().run() 





<Fondo>:
    scroll_view: scrollviewID
    listgrid: gridlayoutID
    textbox: textboxID
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1,0.1
        pos_hint: {'top':1}
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'Nombre'
            TextInput:
                id: textboxID
                multiline: False
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1,0.8
        pos_hint: {'top':0.9}
        canvas:
            Color:
                rgba: (0.2, 0.2, 0.2, 1)
            Rectangle:
                pos: self.pos
                size: self.size
        ScrollView:
            id: scrollviewID
            orientation: 'vertical'
            pos_hint: {'x': 0, 'y': 0}
            bar_width: '20dp'
            GridLayout:
                id: gridlayoutID
                cols: 1
                size_hint: 1, None
                row_default_height: 40
                row_force_default: False
                BoxLayout:
                    canvas:
                        Color:
                            rgba: (0.4, 0.4, 0.4, 1)
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    Label:
                        text: 'Nombre'
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1,0.1
        pos_hint: {'top':0.1}
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: 'Guardar'
                on_release: root.OnGuardarClick(textboxID.text)
            Button:
                text: 'Exportar'
                on_release: root.OnExportarClick()
