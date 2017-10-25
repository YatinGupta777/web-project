from django.conf.urls import url
from fbfeed import views


app_name='fbfeed'
urlpatterns =[
    url(r'^$',views.FbPostsView.as_view(),name='fbPosts'),
]
