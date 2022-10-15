from datetime import datetime
from django.db import models


class Choice(models.Model):
    """Варианты ответов"""

    # poll = models.ForeignKey('Poll', on_delete=models.CASCADE, verbose_name="Опрос")
    name = models.CharField(verbose_name="Вариант ответа", max_length=20)

    def __str__(self):
        return self.name

class Poll(models.Model):
    """Таблица опросов"""

    name = models.CharField(verbose_name="Название опроса", max_length=50)
    description = models.TextField(verbose_name="Описание опроса",)
    choices = models.ManyToManyField(Choice, verbose_name="Вариант ответа", related_name='poll_choices', blank=True)

    def __str__(self):
        return self.name

class Vote(models.Model):
    """Таблица ответов"""

    poll = models.ForeignKey(Poll, verbose_name="Опрос", on_delete=models.SET_NULL, related_name='vote_poll', null=True, blank=True)
    choice = models.ForeignKey(Choice, verbose_name="Выбранный вариант ответа", related_name='vote_choice', on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(verbose_name="Время ответа", default=datetime.now)

    def __str__(self):
        return f"{self.pk}"

