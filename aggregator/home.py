import os
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from PIL import Image
from aggregator.forms import Aggregator, TagsForm
from aggregator.models import Articles, ArticleImages, Tags, Categories
from datetime import datetime, timedelta
import time
import urllib2, urllib
from django.views.decorators.csrf import csrf_exempt
from django.template.defaultfilters import slugify

def index(request):
		'''Show the posts for administering'''
		form = Aggregator() #Stop using this form for displaying forms.  This is too dependant on the framework and no benefit
		d = datetime.now()
		week_ago = timedelta(days=60)
		start_day = d-week_ago #get date from a week ago
		news_dict = {}
		#news_roll = Articles.objects.filter(publish_datetime__gte=start_day).order_by('-publish_datetime', '-created_at')
		news_roll = Articles.objects.all().order_by('-created_at','-publish_datetime')[:30]
		order_arr = []
		for news in news_roll:
			news_dict = {}
			news_dict['id'] = news.id
			news_dict['news_info'] = news
			news_dict['article_short'] = news.article_text[:100]
			news_dict['article_date'] = make_readable_date(news.publish_datetime)
			images = ArticleImages.objects.filter(articles=news)
			news_dict['images'] = {}
			images = split_images(images)
			news_dict['first_cat'] = get_first_matching_category(news.id)
			news_dict['images'] = images
			news_dict['featured_image'] = get_featured_image(news.mainthumb)
			order_arr.append(news_dict)
		hours = get_hours()
		minutes = get_minutes()
		context = {'news_dict': news_dict, 'ordered_arr': order_arr, 'hours': hours, 'minutes': minutes}
		return render(request, 'aggregator/home/index.html', context)

def make_readable_date(raw_date):
		if raw_date:
				p_date_arr = str(raw_date).split("+")
				p_date = time.strptime(p_date_arr[0], "%Y-%m-%d %H:%M:%S")	
				readable_date = time.strftime("%b %d, %Y", p_date)
				return str(readable_date)
		return "None"

def get_first_matching_category(news_id):
		if news_id:
				category = Categories.objects.filter(articles_id=news_id)
				for categor in category:
						return categor.categoryname
		return ''

def get_featured_image(image_id=None):
		if image_id:
				article_image = ArticleImages.objects.get(pk=image_id)
				image_name_arr = article_image.image_name.split(".")
				extension = image_name_arr.pop()
				image_name = ".".join(image_name_arr)
				featured_image_dict = {}
				featured_image_dict['link_name'] = article_image.image_link + '/' + image_name
				featured_image_dict['extension'] = extension
				return featured_image_dict
		return "None"

def split_images(images):
		image_list = []
		for image in images:
				f = open("/www/sites/crazyforus.com/aggregator/logfile.txt", "w")
				f.write("%s" % image.image_link)
				f.close()
				image_info = {}
				image_info['image_link'] = image.image_link
				image_name_arr = image.image_name.split('.')
				extension = image_name_arr.pop()
				image_name = ".".join(image_name_arr)
				image_info['image_name'] = image_name
				image_info['extension'] = extension
				image_list.append(image_info)
		return image_list
				
def get_minutes():
		minutes = ""
		for i in range(0,61):
				minutes+="<option>%s</option>\n" % i
		return minutes

def get_hours():
		hours = ""
		for i in range(0,25):
				hours+="<option>%s</option>\n" % i
		return hours


