
import inspect,os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.size=(400,130)

class Formulario(GridLayout):
	lista=[]

	def __init__(self, **kwargs):
		super(Formulario, self).__init__(**kwargs)
		self.cols=2
		
		self.add_widget(Label(text='Nombre'))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)
		btn_guardar = Button(text=('Guardar'))
		self.add_widget(btn_guardar)
		btn_guardar.bind(on_press=self.metodo_guardar)
		btn_exportar = Button(text=('Exportar'))
		self.add_widget(btn_exportar)
		btn_exportar.bind(on_press=self.metodo_exportar)
		

	def metodo_guardar(self,evento):
		self.lista.append(self.username.text)
		print(self.lista)
		
	def metodo_exportar(self,evento):
		print(self.lista)
		f_path=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		try:
			zz = open(f_path+ "/asistencia.txt","a+")
			zz.write("\nNombres: "+ str(self.lista) )

		except IOError:
			print("\nNo se ha podido crear el fichero asistencia.txt")
		else:
			print("\nEl archivo asistencia.txt se ha creado correctamente.")
		zz.close()

class AsistenciaApp(App):
	def build(self):
		self.title="Lista de asistencia"
		return Formulario()

if __name__ == '__main__':
	AsistenciaApp().run()
