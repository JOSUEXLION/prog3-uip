

#josuedeleon
#8-876-2357
#parcial 1 
#mi parcial consiste en una calculadora sencilla

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
Window.clearcolor = (0, 0, 0, 0.1)

class Calculadora(BoxLayout):
	def Borrar(self, operacion):
			self.numeros.text = operacion[:-1]

	def Del(self, operacion):
			self.numeros.text = operacion[:0]


	def Calculos(self, operacion):
		try:
			self.numeros.text = str( eval(operacion))
			print (operacion)
			print (self.numeros.text)
		except:
			self.numeros.text = 'Error de sintaxis'

class CalculadoraApp(App):
	title = "Calpy"
	def build(self):
		return Calculadora()

if __name__ in ('__main__', '__android__'):
	CalculadoraApp().run()
