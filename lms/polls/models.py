from datetime import datetime
from django.db import models


class Choice(models.Model):
    """Варианты ответов"""

    name = models.CharField(verbose_name="Вариант ответа", max_length=20)

    def __str__(self):
        return self.name


class Poll(models.Model):
    """Таблица опросов"""

    name = models.CharField(verbose_name="Название опроса", max_length=50)
    description = models.TextField(verbose_name="Описание опроса", )
    choices = models.ManyToManyField(Choice, verbose_name="Вариант ответа", related_name='related_polls', blank=True)

    def __str__(self):
        return self.name


class Vote(models.Model):
    """Таблица ответов"""

    poll = models.ForeignKey(Poll, models.SET_NULL, verbose_name="Опрос",  null=True, blank=True)
    choice = models.ForeignKey(Choice, verbose_name="Выбранный вариант ответа", on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(verbose_name="Время ответа", default=datetime.now)

    def __str__(self):
        return f"{self.poll.name} - {self.choice.name}"
