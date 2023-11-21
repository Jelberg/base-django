from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Poll, Choice, Vote

def index(request):
    latest_polls = Poll.objects.order_by('-date')[:5]
    context = {'latest_polls': latest_polls}
    return render(request, 'index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'details.html', {'poll': poll})

def vote(request, poll_id):
    
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        print(request.POST['choice'])
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        print('EXCEPTION')
        return render(request, 'details.html', {
            'poll': poll,
            'error_message': "You didn't select a choice.",
        })
    else:
        print('despues del else')
        print(poll)
        Vote.objects.create(poll=poll, choice=selected_choice)
        return HttpResponseRedirect(reverse('results', args=(poll.id,)))

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'results.html', {'poll': poll})