from .abstr_Figure import Figure
from .Colour import Colour

class Rectangle(Figure, Colour):
	name = 'Прямоугольник'
	"""Rectangle - прямоугольник"""
	def __init__(self, a, b, col):
		self.a = a
		self.b = b
		self.col = Colour(col)

	def area(self):
		return self.a * self.b

	def __repr__(self):
		return "Фигура - {}, имеет стороны a = {}, b = {}, площадь - {}, цвет - {}".format(self.name, 
			self.a, self.b , self.area(), self.col.get())