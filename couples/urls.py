from django.conf.urls import patterns, url
from couples import views

urlpatterns = patterns('',
		#/viewpics/
		url(r'^$', views.index, name='index'),
		url(r'^(?P<members_id>\d+)/$', views.index, name='couples_page'),
		url(r'^upload/hero/(?P<members_id>\d+)/$', views.upload_main_pic, name='upload_main_pic'),
		url(r'^welcome/$', views.welcome, name='welcome'),
		url(r'^our_stories/$', views.our_stories, name='our_stories'),
		url(r'^update_stories/$', views.update_stories, name='update_stories'),
)

