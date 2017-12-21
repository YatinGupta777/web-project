from django.conf.urls import url

from . import views

app_name = 'discussion'
urlpatterns = [
    url(r'^Advices/$',views.AdvicesView.as_view(),name="advices"),
]
