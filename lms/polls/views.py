from django.shortcuts import render

# Create your views here.
from django.views import View

from .models import Poll, Choice, Vote


class PollsView(View):

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

    def get(self, request, poll_id):
        poll = Poll.objects.get(id=poll_id)
        return render(
            request,
            template_name="polls/pages/poll.html",
            context={
                "poll": poll,
            }
        )

    def post(self, request, poll_id):
        requestData = request.POST

        choice_id = requestData.get('choice_id')

        poll = Poll.objects.get(id=poll_id)
        choice = Choice.objects.get(id=choice_id)
        Vote.objects.create(
            poll=poll,
            choice=choice,
        )

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
