from django.conf.urls import url
from lists import views

urlspatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
]