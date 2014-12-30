from django.conf.urls import patterns, url
from register import views

urlpatterns = patterns('',
		#/viewpics/
		url(r'^$', views.index, name='index'),
		url(r'^add/$', views.register, name="register_add"),
		url(r'^getcity/$', views.getcity, name="getcity"),
		url(r'^websitecheck/$', views.websitecheck, name="websitecheck"),
		url(r'^(?P<template>.+)/$', views.register, name="register")
)

