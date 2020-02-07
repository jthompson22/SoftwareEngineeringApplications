from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import DataField

def index(request):
    latest_field_list = DataField.objects.order_by('-pub_date')[:5]
    template = loader.get_template('SubmissionForm/index.html')
    context = {
        'latest_field_list':latest_field_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = DataField.objects.get(pk=question_id)
    except DataField.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'SubmissionForm/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(DataField, pk=question_id)
    return render(request, 'SubmissionForm/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(DataField, pk=question_id)
    try:
        selected_choice = question.datainput_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'SubmissionForm/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.data_nums += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('SubmissionForm:results', args=(question.id,)))
