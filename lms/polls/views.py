from django.shortcuts import render

# Create your views here.
from django.views import View

from .models import Poll, Choice, Vote


class PollsView(View):
    """Вывод списка существующих опросов"""

    def get(self, request):
        polls = Poll.objects.all()
        return render(
            request,
            template_name="polls/pages/polls.html",
            context={
                "polls": polls,
            }
        )


class PollView(View):
    """Работа с конкретным опросом по id"""


    def get(self, request, poll_id):
        """Отдача опроса"""

        poll = Poll.objects.get(id=poll_id)
        return render(request, template_name="polls/pages/poll.html", context={"poll": poll,})

    def post(self, request, poll_id):
        """Обработка формы"""

        requestData = request.POST

        choice_id = requestData.get('choice_id')

        poll = Poll.objects.get(id=poll_id)
        choice = Choice.objects.get(id=choice_id)
        Vote.objects.create(poll=poll, choice=choice,)

        # формирование статистики по опросу "ответ-сколько человек его выбрали"
        poll_results = []
        for choice in poll.choices.all():
            voteCount = Vote.objects.filter(poll=poll, choice=choice).count()
            poll_results.append([choice.name, voteCount])

        return render(
            request,
            template_name="polls/pages/poll.html",
            context={
                "poll": poll,
                "success_message": "Voted Successfully",
                "poll_results": poll_results,
            }
        )
