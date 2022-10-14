from django.core.management.base import BaseCommand
from polls.models import *
from django.contrib.auth.models import User


class Command(BaseCommand):
    """Создание опросов"""

    polls_list_data = [{"poll": {"name": "Кто лучше кошки или собаки?",
                                 "description": "Это опрос про животных",
                                 },
                        "choices": [
                            {"name": "Кошки"},
                            {"name": "Собаки"},
                            {"name": "Другие животные"}, ]
                        },
                       {"poll": {"name": "Работать или не работать вот в чем вопрос?",
                                 "description": "Опрос на тему 'как вы проводите рабочее время'",
                                 },
                        "choices": [
                            {"name": "Да, конечно работать"},
                            {"name": "Нет, не стоит напрягаться"},
                            {"name": "Затрудняюсь ответить"}, ]
                        },
                       ]


    def __create_poll(self, one_poll):
        """Создать один опрос"""

        # one_poll = {"poll": {"name": "Марии Константиновна",
        #                      "description": "Ржев",
        #                      },
        #             "choices": [
        #                 {"name": "1 Марии Константиновна"},
        #                 {"name": "2 Марии Константиновна"},
        #                 {"name": "3 Марии Константиновна"},]
        #             }

        # достанем данные из объекта
        poll_data = one_poll.get("poll")
        list_of_choices_data = one_poll.get("choices")

        # создадим опрос
        poll, status = Poll.objects.get_or_create(**poll_data)

        # cоздадим варианты ответа и добавим к опросу
        for choice_data in list_of_choices_data:
            choice, status = Choice.objects.get_or_create(**choice_data)
            poll.choices.add(choice)

    def _create_polls(self):
        """Создать несколько опросов"""

        for poll_data in self.polls_list_data:
            self.__create_poll(one_poll=poll_data)

    def handle(self, *args, **options):
        """В каком порядку выполняем"""

        self._create_polls()