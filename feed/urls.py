from django.conf.urls import url
from feed import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

app_name='feed'
urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name="post_list"),
    url(r'^notes/$',views.Notes.as_view(),name="notes"),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/new/$',views.CreatePostView.as_view(),name ='post_new'),
    url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),
    url(r'^login/',views.home, name='login'),
    url(r'^map/$',views.MapView.as_view(),name='map'),
    

    url(r'^postAPI/$',views.PostList.as_view(),name="post_API"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
