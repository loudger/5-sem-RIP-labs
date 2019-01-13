from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=80, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание')
    image = models.ImageField(verbose_name='Картинка')


class Game(models.Model):
    # team_one = models.ForeignKey(
    #     'Team',
    #     on_delete=models.CASCADE,
    #     related_name='first_team'
    # )

    # team_two = models.ForeignKey(
    #     'Team',
    #     on_delete=models.CASCADE,
    #     related_name='second_team'
    # )
    team_one = models.CharField(max_length=80, verbose_name='Первая команда')
    team_two = models.CharField(max_length=80, verbose_name='Вторая команда')
    description = models.CharField(max_length=255, verbose_name='Описание')
    game_date = models.DateTimeField(verbose_name='Дата игры')

