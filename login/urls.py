from django.conf.urls import patterns, url
from login import views

urlpatterns = patterns('',
		#/viewpics/
		url(r'^$', views.index, name='index'),
		url(r'^signin/$', views.login, name='signin'),
)

