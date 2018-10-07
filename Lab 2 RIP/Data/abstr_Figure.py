from abc import ABCMeta, abstractmethod

"""PEP8"""
class Figure (metaclass = ABCMeta):
	"""Абстрактный класс Геометр.Фигура"""
	@abstractmethod
	def area (self):
		pass
	@abstractmethod
	def __repr__(self):
		pass