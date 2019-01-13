from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import TemplateView
from HomePage.models import Game
from django.shortcuts import render


# LoginView
class HomePageView(TemplateView):
    template_name = 'Game_list/Games_list_view.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['games'] = Game.objects.all().order_by('id')
        return data

# class UserLoginView(LoginView):
#     template_name = 'login.html'
#     form_class = LoginForm
#     redirect_authenticated_user = True
#
#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         data['form_action'] = reverse('login')
#         return data
#
#     def get_success_url(self):
#         return reverse('task_list')


# class BetsListView(LoginRequiredMixin, TemplateView):
#     template_name = ''      #html


