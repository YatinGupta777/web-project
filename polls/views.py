from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from polls.models import Choice,Question
from django.views.generic import CreateView
from polls.forms import ChoiceForm
from braces.views import SelectRelatedMixin

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.all#.filter(
        #    publish_date__lte = timezone.now()
        #)#.order_by('publish_date')[:5]

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice  = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        #Redisplay the question voting form
        return render(request,'polls/index.html',{
            'question':question,
            'error_message':"You didnt select a choice",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:index'))

class CreateChoice(CreateView):
        redirect_field_name = 'polls/index.html'
        template_name = 'polls/poll_form.html'
        form_class = ChoiceForm
        model = Choice
        select_related = ('question_text','choice_text')
