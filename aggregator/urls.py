from django.conf.urls import patterns, url
from aggregator import views, home, wp_home, sidebar

urlpatterns = patterns('',
		#Aggregator View stuff
		url(r'^$', wp_home.index, name='index'),
		url(r'^test_image/$', views.test_image, name='test'),
		url(r'^article/$', views.single_article, name='single_article'),
		url(r'^home/$', home.index, name='home_index'),
		url(r'^wp_home/$', wp_home.index, name='wp_index'),
		#Test Stuff
		url(r'^edit_article_images_test/(?P<article_id>.+)/$', views.edit_article_images_test, name="edit_article_images"),
		#/aggregator Admin Below
		url(r'^admin/$', views.admin, name='admin_index'),
		url(r'^add/$', views.add, name="admin_add"),
		url(r'^fetchimage/$', views.fetchImage, name="fetch_image"),

		#category stuff
		url(r'^admin/get_categories/$', views.get_categories, name="get_categories"),
		url(r'^admin/get_categories_list/(?P<article_id>.+)/$', views.get_categories_list, name="get_categories"),
		url(r'^admin/addcategory/$', views.add_category, name="add_category"),
		url(r'^admin/update_category/(?P<article_id>.+)/$', views.add_or_remove_cat, name="update_article_category"),

		#edit article
		url(r'^delete_recent/$', views.delete_recent, name="delete_recent"),
		url(r'^delete/(?P<article_id>.+)/$', views.delete_article, name="delete_article"),
		url(r'^edit/(?P<article_id>.+)/$', views.edit_article, name="edit_article"),
		url(r'^crop_article_images/(?P<article_id>.+)/$', views.edit_article_images, name="crop_article_images"),
		url(r'^edit_article_images/(?P<article_id>.+)/$', views.edit_article_images, name="edit_article_images"),
		url(r'^edit_article_images/$', views.edit_article_images, name="edit_article_images_crop"),
		url(r'^crop_article_images/$', views.edit_article_images, name="edit_article_images_crop"),
		url(r'^set_feature_pic/(?P<article_id>.+)/$', views.set_feature_pic, name="set_feature_pic"),

		#Misc
		url(r'^test_images/$', views.make_eight_imgs, name="non_edit_article_images_crop"),
		url(r'^update/(?P<article_id>.+)/$', views.update_article, name="update_article"),
		url(r'^article/(?P<article_id>.+)/$', views.show_article, name="show_article"),
		url(r'^category/$', wp_home.category_view, name="category"),
		url(r'^category/(?P<category>.+)/$', wp_home.category_view, name="category"),
		url(r'^article/(?P<article_id>.+)/$', views.show_article, name="show_article"),

		#sidebar mgmt 
		url(r'^sidebar/$', sidebar.index, name="sidebar"),
)

