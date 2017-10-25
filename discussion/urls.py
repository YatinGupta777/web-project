from django.conf.urls import url

from . import views

app_name = 'discussion'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
