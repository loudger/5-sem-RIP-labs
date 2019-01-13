from django.shortcuts import render
from django.views import View


# def index(request):
#     return HttpResponse('<h3>Привет мир!</h3>')


class MyView(View):
	def get(self, request):
		data = {
			'orders': [
				{'title': 'Первый заказ', 'id': 1},
				{'title': 'Второй заказ', 'id': 2},
				{'title': 'Третий заказ', 'id': 3}
			]
		}
		return render(request, 'myapp/html/orders.html', data)



class OrderView(View):
	def get(self, request, id):
		data = {
			'order': {
				'id': id
			}
		}
		return render(request, 'myapp/html/order.html', data)