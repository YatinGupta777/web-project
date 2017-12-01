from django.conf.urls import  url
from django.contrib.auth import views as auth_views
#LOGIN AND LOGOUT VIEWS PRE DEFINED
#imported as auth_views so to clearly diffrenetiate betwen our views
from . import views


app_name='accounts'
urlpatterns = [
    url(r'login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),
    url(r'signup/$',views.Signup.as_view(),name='signup'),
    url(r'^login_methods/',views.home, name='login_methods'),
    url(r'^user_info/$',views.UserInfo.as_view(),name='user_info'),
]
