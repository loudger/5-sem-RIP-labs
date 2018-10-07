from .abstr_Figure import Figure
from .Colour import Colour
from math import pi


class Circle(Figure):
	def __init__(self, r, col):
		self.r = r
		self.col = Colour(col)
		self.name = 'Круг'
	def __repr__(self):
		return "Фигура - {}, имеет стороны a = {}, площадь - {}, цвет - {}".format(self.name, 
			self.a, self.area(), self.col)
	def area(self):
		return (self.r ** 2 )* pi

	def __repr__(self):
		return "Фигура - {}, имеет радиус r = {}, площадь - {:.2f}, цвет - {}".format(self.name, 
			self.r, self.area(), self.col.get())