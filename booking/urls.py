from django.conf.urls import url
from . import views

app_name = 'booking'

urlpatterns = [
    url(r'book/$', views.BookUI, name='book'),
    url(r'confirm/$', views.ConfirmUI, name='confirm'),
    url(r'history/$', views.HistoryUI, name='history')
]
