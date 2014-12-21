from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
		(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':'/www/sites/crazyforus.com/static/'}),
		(r'^ckeditor/(?P<path>.*)$','django.views.static.serve',{'document_root':'/www/sites/crazyforus.com/ckeditor/'}),
		(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':'/www/sites/crazyforus.com/media/'}),
    # url(r'^$', 'crazyforus.views.home', name='home'),
    # url(r'^crazyforus/', include('crazyforus.foo.urls')),

		# HOME
		url(r'^aggregator/', include('aggregator.urls')),
		url(r'^$', 'aggregator.wp_home.index', name='index'),

		# Article
		url(r'^articles/(?P<article_name>.*)$', 'aggregator.wp_home.show_article', name='show_article'),

		# Categories
		url(r'^category/$', 'aggregator.wp_home.category_view', name="category"),
		url(r'^category/(?P<category>.+)/$', 'aggregator.wp_home.category_view', name="category"),

		# Search
		url(r'^search/(?P<search_term>.+)/$', 'aggregator.wp_home.search_view', name="search_view"),
		url(r'^search/$', 'aggregator.wp_home.search_view', name="search_view"),


		# Sign-up login
		url(r'^register/', include('register.urls')),
		url(r'^login/', include('login.urls')),
		url(r'^couples/', include('couples.urls')),
		#url(r'^vendors/', 'vendors.views.index', name='vendors'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
