import os, sys
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from PIL import Image
from aggregator.models import Articles, Category
from aggregator.wp_models import WpPosts, WpTerms, WpTermTaxonomy, WpTermRelationships, WpPostmeta
from datetime import datetime, timedelta
import time
import urllib2, urllib
from django.views.decorators.csrf import csrf_exempt
from django.template.defaultfilters import slugify
import MySQLdb as mdb

def index(request):
		base = '/www/sites/crazyforus.com/aggregator/templates/aggregator/home/' 
		if request.method == "POST":
				s = open(base+'sidebar.html')
				f = open(base+'wp_index.html', "w")
				fullFile = f.read()
				start = fullFile.find("<!-- manage sidebar")
				end = fullFile.find("<!-- end manage sidebar")
				end = fullFile.find(">", end) 
				subset = fullFile.substring(fullFile, start, end)
				newstuff = request.POST['sidebar']
				fullFile.replace(subset, newstuff)
				f.write(fullFile)
				f.close()
				context = {'sidebar': fullFile}
				return render(request, 'aggregator/home/sidebar.html', context)
		f = open(base+'sidebar.html', "rw")
		fullFile = f.read()
		start = fullFile.find("<!-- manage sidebar")
		end = fullFile.find("<!-- end manage sidebar")
		end = fullFile.find(">", end) 
		subset = fullFile[start:end]
		context = {'sidebar': subset}
		return render(request, 'aggregator/home/sidebar.html', context)
