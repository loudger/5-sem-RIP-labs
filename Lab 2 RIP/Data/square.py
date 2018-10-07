from .rectangle import Rectangle
from .Colour import Colour


class Square(Rectangle):
	name = 'Квадрат'
	def __init__ (self, a, col):
		self.a = a
		self.col = Colour(col)

	def area(self):
		return self.a ** 2

	def __repr__(self):
		return "Фигура - {}, имеет стороны a = {}, площадь - {}, цвет - {}".format(self.name, 
			self.a, self.area(), self.col.get())