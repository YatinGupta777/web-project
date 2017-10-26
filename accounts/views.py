from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from .import forms
from django.template.context import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
class Signup(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('feed/login.html',
                             )
#LOGIN AND LOGOUT VIEWS PRE DEFINED by from django.contrib.auth import views as auth_views
#and directly used in urls.py
