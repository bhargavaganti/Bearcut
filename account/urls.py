from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    url(r'signup/$', views.SignupUI.as_view(), name='signup'),
    url(r'login/$', views.LoginUI.as_view(), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout')
]
