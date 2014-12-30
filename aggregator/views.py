import os
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from PIL import Image
from aggregator.forms import Aggregator, TagsForm
from aggregator.models import Articles, ArticleImages, Tags, Category, Categories
from aggregator.wp_models import WpPosts
from datetime import datetime, timedelta
import urllib2, urllib, json
from django.views.decorators.csrf import csrf_exempt
from django.template.defaultfilters import slugify

def index(request):
		return HttpResponse("Done")
		return HttpResponseRedirect('http://admin.crazyforus.com')
		d = datetime.now()
		week_ago = timedelta(days=7)
		start_day = d-week_ago #get date from a week ago
		news_dict = {}
    #news_roll = Articles.objects.filter(publish_datetime__gte=start_day).order_by('-publish_datetime', '-created_at')[:10]
		news_roll = Articles.objects.all().order_by('-publish_datetime', '-created_at')[:19]
		i = 0
		for news in news_roll:
			news_dict[i] = {}
			news_dict[i]['news_info'] = news
			images = ArticleImages.objects.filter(articles=news)
			news_dict[i]['images'] = {}
			news_dict[i]['images'] = images
			i+=1
		article_length = len(news_dict)
		context = {'news_dict': news_dict, 'article_length': article_length}
		return render(request, 'aggregator/index.html', context)

def single_article(request):
		posts = WpPosts.objects.using('wp_crazy').filter(post_parent=0).order_by('-id')[:1]
		content = {'post': posts}
		return render(request, 'aggregator/home/article.html', content)

def show_article(request, article_id):
		if not article_id == None:
			article_dict = {}
			article = Articles.objects.get(pk=article_id)
			article_images = ArticleImages.objects.filter(articles=article)	
			articletags = Tags.objects.filter(articles=article)
			data = {'title': article.title,
									'article_text': article.article_text, 'source_name': article.source_name,
									'source_link': article.source_link
							}
			form = Aggregator(data)
			article_dict = {'art': article, 'art_images': article_images}
			pub_time = article.publish_datetime
			context = {'data': data, 'art_images': article_images, 'article_id': article_id, 'tags': articletags}
			return render(request, 'aggregator/article.html', context)
		else:
				pass
		return HttpResponseRedirect('/')
						

def admin(request):
		'''Show the posts for administering'''
		form = Aggregator() #Stop using this form for displaying forms.  This is too dependant on the framework and no benefit
		d = datetime.now()
		week_ago = timedelta(days=60)
		start_day = d-week_ago #get date from a week ago
		news_dict = {}
		#news_roll = Articles.objects.filter(publish_datetime__gte=start_day).order_by('-publish_datetime', '-created_at')
		news_roll = Articles.objects.all().order_by('-created_at','-publish_datetime')
		categories = Category.objects.all().order_by('name')
		order_arr = []
		for news in news_roll:
			news_dict = {}
			news_dict['id'] = news.id
			news_dict['news_info'] = news
			news_dict['article_short'] = news.article_text[:100]
			images = ArticleImages.objects.filter(articles=news)
			news_dict['images'] = {}
			images = split_images(images)
			news_dict['images'] = images
			order_arr.append(news_dict)
		hours = get_hours()
		minutes = get_minutes()
		context = {'categories': categories, 'news_dict': news_dict, 'ordered_arr': order_arr, 'hours': hours, 'minutes': minutes}
		return render(request, 'aggregator/admin/admin.html', context)
	
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
				

def split_image_name(image):
		image_name_arr = image.split('.')
		extension = image_name_arr.pop()
		image_name = ".".join(image_name_arr)
		return image_name, extension

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

def add(request):
		if request.method == 'POST':
				article_id = 1
				pub_datetime = request.POST['publish_datetime']
        #pub_datetime = request.POST['publish_datetime'] + " " + request.POST['hour'] + ":" + request.POST['minutes'] + ":00"
				#save the new article
				#TODO make slug title unique
				slug_title = slugify(request.POST['article-title'])
				article = Articles(title=request.POST['article-title'], slug=slug_title, article_text=request.POST['article_text'],
            source_name=request.POST['source_name'], source_link=request.POST['source_link'],
            publish_datetime=pub_datetime)
				article.save()
				#save any categories related to this article
				if 'category_check' in request.POST:
						check_list = request.POST.getlist('category_check')
						for category in check_list:
								cat = Categories(articles=article, categoryname=category)
								cat.save() 
				article_id = article.id
				post_dict = request.POST.dict()
				has_files = save_all_images(request, article)
				for key in post_dict:
						if key[:18] == "article_image_name":
								article_image = ArticleImages(articles=article, image_link=file_location_rel, image_name=request.POST[key])
								article_image.save()
						if key == "tags":
								if request.POST["tags"]:
										tags = request.POST["tags"]
										tags_arr = tags.split(",")
										for tag in tags_arr:
												addtag = Tags(articles=article, tagname=tag.strip())
												addtag.save()
				if has_files:
						return HttpResponseRedirect('/aggregator/edit_article_images/'+ str(article_id) +'/')
				else:
						return HttpResponseRedirect('/aggregator/admin/')
		else:
				form = Aggregator()
				context = {'form': form}
				return render(request, 'aggregator/admin.html', context)
		#Return to manage images
		return HttpResponseRedirect('/aggregator/admin/')

''' Provides a list of images related to the article id provided '''
@csrf_exempt
def get_article_image_list(request, article_id=None):
		if article_id:
				images = ArticleImages.objects.filter(articles_id=article_id)
				return HttpResponse(images)
		return HttpResponse('no id')

def save_all_images(request, article):
		'''  This will save all files that have been uploaded to the article_images table and 
			it will also create a place for them to live (folder) 
		'''
		MEDIA_ROOT = '/www/sites/crazyforus.com/media'
		SITE_ROOT = '/media'
		file_location = get_date_directory(MEDIA_ROOT)
		file_location_rel = urllib.quote("/media"+file_location.replace(MEDIA_ROOT, ""))
		#Check to see if any images have been uploaded
		if request.FILES:
				x = int(request.POST['num_images'])
				i = 1
				while i <= x:
						file = request.FILES.get('uploaded_file_%s' % i).read()
						filename = request.FILES.get('uploaded_file_%s' % i).name
						filename = find_unique_filename(file_location, filename)
						f = open(file_location+'/'+filename, 'w')
						f.write(file)
						f.close()
						article_image = ArticleImages(articles=article, image_link=file_location_rel, image_name=filename)
						article_image.save()
						i += 1
				return True
		return False

def update_article(request, article_id=None):
		if not article_id == None and request.method == 'POST':
				pub_datetime = request.POST['publish_datetime']
				#pub_datetime = pub_datetime.strftime("%Y-%m-%d %H:%M:%S")	
				article = Articles.objects.get(pk=article_id)
				article.title = request.POST['title']
				article.article_text = request.POST['article_text']
				article.source_name = request.POST['source_name']
				article.source_link = request.POST['source_link']
				article.publish_datetime = pub_datetime
				article.save()
				has_files = save_all_images(request, article)
				if has_files:
						return HttpResponseRedirect('/aggregator/edit_article_images/'+ str(article_id) +'/')
				return HttpResponseRedirect('/aggregator/edit/%s' % article_id +'/') 
		else:
				return HttpResponseRedirect('/aggregator/admin/')

@csrf_exempt
def set_feature_pic(request, article_id=None):
		if article_id:
				''' Set the mainthumb field in articles table with the relative
				link to the featured image '''
				img_id = int(request.POST['img_id'])
				this_art = Articles.objects.get(pk=article_id)
				this_art.mainthumb = img_id
				this_art.save()
				return HttpResponse('success')
		return HttpResponse('failed')
		
def edit_article(request, article_id=None):
		if not article_id == None:
				article_dict = {}
				article = Articles.objects.get(pk=article_id)
				article_images = ArticleImages.objects.filter(articles=article) # article related images	
				articletags = Tags.objects.filter(articles=article) # These are basically article categories
				# The below data is the article related data
				data = {'title': article.title,
										'article_text': article.article_text, 'source_name': article.source_name,
										'source_link': article.source_link
								}
				article_dict = {'art': article, 'art_images': article_images}
				hours = get_hours()
				minutes = get_minutes()
				pub_time = article.publish_datetime
				pub_date = pub_time.strftime("%Y-%m-%d")
				curr_hour = pub_time.strftime("%H")
				curr_min = pub_time.strftime("%M")
				tags = get_tags(articletags)
				tags = ",".join(tags)
				context = {'article_data': data, 'art_images': article_images, 'article_id': article_id, 'pub_date': pub_date, 'hours': hours, 'minutes': minutes,
								'tags': tags, 'curr_hour': curr_hour, 'curr_min': curr_min}
				return render(request, 'aggregator/admin/edit.html', context)
		else:
				return HttpResponseRedirect('/aggregator/admin/')

def edit_article_images_test(request, article_id=None):
		''' this is a call to crop the images of this post.  It will be cropped and
		 resized to 12 different sizes - at some point this could be more clever than
		 it is.  As in useing the width and height for restrictions on what can be
		cropped.  The article should no if it has the correct images to be a part of a type of post '''
		#x1, x2, y1, y2 = int(float(request.GET['x1'])), int(float(request.GET['x2'])), int(float(request.GET['y1'])), int(float(request.GET['y2']))
		x1, x2, y1, y2 = 0, 900, 20, 500 
		coords = [x1, y1, x2,y2]
		image_url = '/media/aggregator/TEST-3.jpg'
		image_url_arr = image_url.split(".")
		image_loc = '/www/sites/crazyforus.com' + image_url
		result = make_eight_imgs(image_loc, coords);
		return render(request, 'aggregator/admin/edit_test.html', {'image_location': image_url_arr})


@csrf_exempt
def edit_article_images(request, article_id=None):
		if request.method == "POST":
				''' this is a call to crop the images of this post.  It will be cropped and
				 resized to 12 different sizes - at some point this could be more clever than
				 it is.  As in useing the width and height for restrictions on what can be
				cropped.  The article should no if it has the correct images to be a part of a type of post '''
				x1, x2, y1, y2 = int(float(request.POST['x1'])), int(float(request.POST['x2'])), int(float(request.POST['y1'])), int(float(request.POST['y2']))
				coords = [x1, y1, x2,y2]
				image_loc = '/www/sites/crazyforus.com' + request.POST['image_url']
				result = make_eight_imgs(image_loc, coords);
				return HttpResponse("success"); 
		if not article_id == None:
				article = Articles.objects.get(pk=article_id)
				article_images = ArticleImages.objects.filter(articles=article) # article related images	
				img_list = ''
				img_size_list = ''
				for img in article_images:
						img_tog = img.image_link + '/' + img.image_name
						img_list = img_list+img_tog+','
						image = Image.open('/www/sites/crazyforus.com/'+img_tog)
						img_size_list = img_size_list + str(image.size[0])+'_'+str(image.size[1])+','
						img.cropped = 1
						img.save()
						
				context = {'article_id': article_id, 'article_images': article_images, 'image_size_list': img_size_list, 'img_list': img_list}
				return render(request, 'aggregator/admin/edit_article_images.html', context)
		return HttpResponseRedirect('/aggregator/admin/')

def make_eight_imgs(main_image, coords):
		img =  Image.open(main_image)
		box = (coords[0], coords[1], coords[2], coords[3])
		orig_x = img.size[0]
		orig_y = img.size[1]
		orig_size = [orig_x, orig_y]
		#img = img.crop(box)
		img_arr = main_image.split(".")
		extension = img_arr.pop()
		main_image = ".".join(img_arr)
		new_main_file = main_image+'_819x470.'+extension
		#img.thumbnail((819, 470), Image.ANTIALIAS)
		#img.save(new_main_file)
		size_list = ['819x452','100x80', '570x452','115x115', '120x105', '170x150', '265x165', '265x160', '300x200', '334x301', '350x150', '560x490', '75x75', '770x470']
		for size in size_list:
				size_image(main_image, size, extension, orig_size, coords)
		return True

def size_image(main_img, siz, extension, orig_size, coords):
		''' Receive the base image name the size and the extension which will give you an appropriate name
			This needs to decide which way to resize and crop the image.  Grabbing from the middle would be 
			best.  Size 819x470 is the default '''
		w_h_arr = siz.split('x')	
		w = int(w_h_arr[0])
		h = int(w_h_arr[1])
		new_ratio = w/h
		orig_ratio = orig_size[0]/orig_size[1]
		img = Image.open(main_img+'.'+extension)
		if (h <= w) and (orig_size[1] >= orig_size[0]):
				w_ratio = float(w)/orig_size[0]
				new_height = int(orig_size[1]*w_ratio)
				img = img.resize((int(w), int(new_height)), Image.ANTIALIAS)
				x1 = 0
				x2 = int(w)
				y1 = int(coords[1]*w_ratio)
				y2 = y1+int(h)
				box = (x1, y1, x2, y2)
				#f = open('/www/sites/crazyforus.com/aggregator/logcrop.txt', 'a')
				#f.write("Width: " + siz + " - New Height: " + str(new_height) + " - " + str(box)+ " - COORDS: " + str(coords) + "\n")
				#f.close()
				img = img.crop(box)
				img.save(main_img+'_'+siz+'.'+extension)
		else:
				h_ratio = float(h)/orig_size[1]
				new_width = int(orig_size[0]*h_ratio)
				if new_width < int(w):
						h_ratio = float(w)/orig_size[0]
						new_height = int(orig_size[1]*h_ratio)
						img = img.resize((int(w), int(new_height)), Image.ANTIALIAS)
				else:
						img = img.resize( (int(new_width), int(h) ), Image.ANTIALIAS)
				# find middle of image for new crop
				x1 = int(coords[0]*h_ratio)
				y1 = 0
				y2 = int(h)
				x2 = x1+int(w)
				box = (x1, y1, x2, y2)
				f = open('/www/sites/crazyforus.com/aggregator/logcrop.txt', 'a')
				f.write("Height: " + str(main_img) + " - " + siz + " - New Width: " + str(new_width) + " - " + str(box)+ "\n")
				f.close()
				img = img.crop(box)
				img.save(main_img+'_'+siz+'.'+extension)

def get_tags(articletags):
		tag_list = []
		for tag in articletags:
				tag_list.append(tag.tagname)
		return tag_list

def delete_images(art_images):
		''' cycle through object and delete related images '''
		MEDIA_ROOT = '/www/sites/crazyforus.com/media'
		for image in art_images:
				filename = MEDIA_ROOT+"/"+image.image_link+"/"+image.image_name
				if os.path.exists(filename):
						os.delete(filename)

def delete_article(request, article_id=None):
		if not article_id == None:
				art_images = ArticleImages.objects.filter(articles=article_id)
				delete_images(art_images)
				article = Articles.objects.get(pk=article_id)
				article.delete()
		return HttpResponseRedirect('/aggregator/admin/')	

@csrf_exempt
def delete_recent(request):
		''' Delete an individual image from a post '''
		if request.method == 'GET':
				if not request.GET['imageid'] == '':
						art_image_id = request.GET['imageid']
						base_location = '/www/sites/crazyforus.com'
						art_image = ArticleImages.objects.get(pk=art_image_id)
						art_image.delete()
						folder = base_location+art_image.image_link
						size_list = ['', '_819x470', '_819x452','_100x80', '_115x115', '_120x105', '_170x150', '_265x165', '_300x200', '_334x301', '_350x150', '_560x390', '_75x75', '_770x470'] 
						image_name, extension = split_image_name(art_image.image_name)
						for size in size_list:
								try:
										os.remove(folder+'/'+image_name+size+'.'+extension)
								except:
										return HttpResponse("Not Deleted: " + folder+'/'+image_name+size+'.'+extension)
						return HttpResponse("file_deleted")
				else:
						return HttpResponse("error")
		return HttpResponse("error")
		
def testupload(request):
		if request.FILES:
				actual_file= request.FILES['file']
				if actual_file:
						fileexist = "True"
				else:
						fileexist = "False"
		context = {'fileexist': fileexist}

		return render(request, 'showerlist/test_upload.html', context)
def fetchImage(request):
		''' Retrieve a file from the interwebs and save it here.
				we'll need to make several size files TODO make thumbnail,
				low_resolution, and standard_resolution files '''
		MEDIA_ROOT = '/www/sites/crazyforus.com/media'
		file_location = get_date_directory(MEDIA_ROOT)
		if request.method == 'GET':
				url = request.GET['url']
				start_of_url = url[:7]
				if not start_of_url == "http://":
						url = "http://"+url
				image_file = urllib2.urlopen(url)
				urlArr = url.split('/')
				filename = str(urlArr[len(urlArr)-1])
				if filename.find("?"):
						filename_arr = filename.split("?")
						filename = filename_arr[0]
				filename = find_unique_filename(file_location, filename)
				f = open('%s/%s' % (file_location,filename), 'w')
				image = image_file.read()
				f.write(image)
				f.close()
				file_location = urllib.quote("/media"+file_location.replace(MEDIA_ROOT, ""))
				return HttpResponse("%s,%s" % (str(filename), file_location))	
		else:
				return HttpResponse("false")

def get_date_directory(base_directory):
		''' Get the current year/month/day and verify that these folders exists.
				if they don't make new ones
        base_directory = (e.g. /www/sites/crazyforus.com) '''
		d = datetime.now() 
		year, month, day = d.strftime("%Y"), d.strftime("%m"), d.strftime("%d")
		folder = "%s/aggregator/images/%s" % (base_directory, year)
		if os.path.exists(folder):
				folder = folder+"/"+month
				if os.path.exists(folder):
						folder = folder+"/"+day 
						if os.path.exists(folder):
								return folder
						else:
								os.makedirs(folder)
								return folder
				else:
						os.makedirs(folder)
						os.makedirs("%s/%s" % (folder, day))
						folder = folder+"/"+day
						return folder
		else:
				os.makedirs(folder)
				os.makedirs("%s/%s" % (folder, month))
				folder = folder+"/"+month
				os.makedirs("%s/%s" % (folder, day))
				folder = folder+"/"+day
				return folder

def get_member_id():
		''' This def will grab the current member id and should be removed by production time.  Another method should be used for authentication and authorization '''
		if 'member_id' in session.request:
				member_id = session.request['member_id']
				return member_id
		else:
				return false

def find_unique_filename(file_location, filename):
		''' This def will return a unique filename in the location provided with a similar name to what is provided '''
		file_list = os.listdir(file_location)	
		if filename in file_list:
				keep_looking = count = 1
				file_arr = filename.split(".")
				new_name = file_arr[len(file_arr)-2]
				new_ext = file_arr[len(file_arr)-1]
				while keep_looking:
						new_filename = "%s-%s.%s" % (new_name, count, new_ext) #creating a new file like imagename-3.jpg
						if not new_filename in file_list:	
								keep_looking = 0
								filename = new_filename
						else:
								count+=1
		return filename

@csrf_exempt
def get_categories_list(request, article_id=None):
		#get cats that have been select for article
		if article_id:
				art_id = article_id
				cats = Category.objects.all()
				cat_list = {}
				for cat in cats:
						cat_list[cat.id] = {}
						cat_list[cat.id]['name'] = cat.name
						categories = Categories.objects.filter(articles=art_id).filter(categoryname=cat.name)
						if categories:
								cat_list[cat.id]['checked'] = 1
						else:
								cat_list[cat.id]['checked'] = 0
				return HttpResponse(json.dumps(cat_list))
		return HttpResponse('wrong call')

@csrf_exempt
def get_categories(request):
		cats = Category.objects.all()
		cats_dict = {}
		for cat in cats:
				cats_dict[cat.id] = cat.name
		cat_json = json.dumps(cats_dict)
		return HttpResponse(cat_json)

@csrf_exempt
def add_category(request):
		if request.method == "GET":
				cat_name = request.GET['category_name']
				try:
						one_cat = Category.objects.get(name=cat_name)
						return HttpResponse('duplicate')
				except:
						cat = Category(name=cat_name)
						cat.save()
						return HttpResponse('added')

@csrf_exempt
def remove_category(request):
		if request.method == "Post" and category_id:
				cat = Category.objects.get(pk=request.POST['category_id'])	
				cat.save()
				return HttpResponse('deleted')
		return HttpResponse('error')

@csrf_exempt
def add_or_remove_cat(request, article_id=None):
		if request.method == "GET" and article_id:
				catid = request.GET['catid']
				cat_once = Category.objects.get(pk=catid)
				article = Articles.objects.get(pk=article_id)
				one_cat = Categories.objects.filter(articles=article).filter(categoryname=cat_once.name)
				if one_cat:
						one_cat.delete()
						return HttpResponse('removed')
				else:
						cat = Categories(articles=article, categoryname=cat_once.name)
						cat.save()
						return HttpResponse('added')
		return HttpResponse(article_id)

@csrf_exempt
def test_image(request):
		x1, x2, y1, y2 = 100, 100, 500, 500
		coords = [x1, y1, x2,y2]
		image_loc = '/www/sites/crazyforus.com/media/aggregator/gold_shoes.jpg'
		img =  Image.open(image_loc)
		img = img.resize((459, 775))
		#img = img.crop((0,100,300,300))
		img.save('/www/sites/crazyforus.com/media/aggregator/gold_shoes_test.jpg')
		return render(request, 'aggregator/admin/test.html')
