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
		# If the old style wordpress request is made we will still handle it.  This will be good for SEO stuff
		if 'p' in request.GET and request.method == "GET":
				wpid = request.GET['p']
				article_dict = {}
				article = WpPosts.objects.using('wp_crazy').filter(id=wpid)
				cats = get_categories(article[0].id)
				break_count = article[0].post_content.count("\n")
				post_content = article[0].post_content.replace("\n", "<br />")
				berta_bridal = make_post_list_by_cat('Berta Bridal')
				boho_style = make_post_list_by_cat('Boho Style')
				claire_petibone = make_post_list_by_cat('Claire Pettibone')
				wedding_hair = make_post_list_by_cat('Wedding Hairstyles', 4)
				seasonal_notables = make_post_list_by_cat('Winter Weddings', 4)
				engagement_rings = make_post_list_by_cat('engagement rings', 4)
				bridal_fashion = make_post_list_by_cat('Bridal Fashion', 4)
				context = {'post_content': post_content, 'post': article, 'categories': cats, 'breakcount': break_count, 'berta_bridal': berta_bridal, 'bridal_fashion': bridal_fashion, 'engagement_rings': engagement_rings, 'wedding_hair': wedding_hair, 'seasonal_weddings': seasonal_notables, 'boho_style': boho_style, 'claire_petibone': claire_petibone}
				return render(request, 'aggregator/home/article_extended.html', context)
		''' This is the home page using the word press db '''
		cat_list = set_all_categories()
		posts = WpPosts.objects.using('wp_crazy').filter(post_parent=0).filter(post_type='post').filter(post_status='publish').exclude(post_title='Auto Draft').order_by('-post_date')[:20]
		post_list = []
		for post in posts:
				post_date = post.post_date.strftime("%b. %d, %Y")
				post_dict = {}
				post_dict['id'] = post.id
				post_dict['title'] = post.post_title
				post_dict['post_date'] = post_date
				post_dict['post_content'] = remove_html(post.post_content, 200)
				post_dict['slug'] = slugify(post.post_name)
				post_dict['images'] = get_post_images(post.id)
				post_dict['categories'] = get_categories(post.id, cat_list)
				post_dict['featured_image'] = get_featured(post.id)
				post_list.append(post_dict)
		berta_bridal = make_post_list_by_cat('Berta Bridal')
		claire_petibone = make_post_list_by_cat('Claire Pettibone')
		diy_news = make_post_list_by_cat('DIY', 4)
		dresses = make_post_list_by_cat('WEDDING DRESSES', 4)
		photo_ideas = make_post_list_by_cat('PHOTO IDEAS', 4)
		centerpieces = make_post_list_by_cat('Centerpieces &amp; Tablescapes', 4)
		wedding_hair = make_post_list_by_cat('Wedding Hairstyles')
		bridal_fashion = make_post_list_by_cat('Bridal Fashion', 4)
		seasonal_notables = make_post_list_by_cat('Winter Weddings', 4)
		seasonal_section = make_post_list_by_cat('Bridesmaids', 4)
		engagement_rings = make_post_list_by_cat('engagement rings', 4)
		#reception_dresses = make_post_list_by_cat('Wedding Reception Dresses')
		context = {'post_list': post_list, 'berta_bridal': berta_bridal, 'bridal_fashion': bridal_fashion, 'claire_petibone': claire_petibone, \
						'diy': diy_news, 'dresses': dresses, 'engagement_rings': engagement_rings, 'wedding_hair': wedding_hair, \
						'centerpieces': centerpieces, 'photo_ideas': photo_ideas, 'seasonal_weddings': seasonal_notables, 'seasonal': seasonal_section}
		return render(request, 'aggregator/home/wp_index.html', context)

def return_nav_articles():
		berta_bridal = make_post_list_by_cat('Berta Bridal')
		boho_style = make_post_list_by_cat('Boho Style')
		claire_petibone = make_post_list_by_cat('Claire Pettibone')
		to_return = "'berta_bridal': %s, 'boho_style': %s, 'claire_petibone': %s" % (berta_bridal, boho_style, claire_petibone)
		return to_return
		
def get_post_images(postid):
		images = WpPosts.objects.using('wp_crazy').filter(post_parent=postid).filter(post_type='attachment').filter(post_mime_type__contains='image')
		image_list = []
		for image in images:
				p_date_arr = str(image.post_date).split(" ")
				p_date = p_date_arr[0]
				p_date = p_date.split("-")
				post_type_arr = image.post_mime_type.split("/")
				if post_type_arr[1] == "jpeg":
						extension = "jpg"
				else:
						extension = post_type_arr[1]
				image_name = image.post_name + "." + extension
				image_link = "http://www.crazyforus.com/wp-content/uploads/%s/%s/%s" % (p_date[0], p_date[1], image_name)
				image_list.append(image_link)
		return image_list

def get_categories(postid, cat_list=None):
		''' This def returns a list of categories related to a particlular post '''
		if cat_list == None:
				cat_list = set_all_categories()
		#three tables involved in this, The cat_list is a list of ids that are actually categories
		objs = WpTermRelationships.objects.using('wp_crazy').filter(object_id=int(postid))
		post_cats = []
		for obj in objs:
				if obj.term_taxonomy_id in cat_list:
						taxonomy = WpTermTaxonomy.objects.using('wp_crazy').get(pk=obj.term_taxonomy_id)
						term_row = WpTerms.objects.using('wp_crazy').get(pk=taxonomy.term_id)
						post_cats.append(term_row.name)
		return post_cats

def set_all_categories():
		#wp_term_taxonomy -> #wp_terms
		catids = WpTermTaxonomy.objects.using('wp_crazy').filter(taxonomy='category')
		category_id_list = []
		for catid in catids:
				category_id_list.append(catid.term_taxonomy_id)
				category = WpTerms.objects.using('wp_crazy').get(pk=catid.term_id)
				try: 
						category = Category.objects.get(name=category.name)
				except:
						Category(name=category.name).save()
		return category_id_list

def get_featured(postid):
		try:
				thumbnail_info = WpPostmeta.objects.using('wp_crazy').filter(meta_key="_thumbnail_id").filter(post_id=postid)
				new_post_id = thumbnail_info[0].meta_value
				featured = WpPostmeta.objects.using('wp_crazy').filter(meta_key='_wp_attached_file').filter(post_id=new_post_id)
				if len(featured):
						image_name = featured[0].meta_value
						image_link = "http://www.crazyforus.com/wp-content/uploads/%s" % image_name
						return image_link
		except:
				image_link = get_first_image(postid)
				return image_link
		else:
				return "None"

def get_first_image(postid):
		post = WpPosts.objects.using('wp_crazy').get(id=postid)
		post_content = post.post_content
		src = post_content.find('src')
		quote = post_content.find('"', src)
		sec_quote = post_content.find('"', quote+1)
		image_link  = post_content[quote+1:sec_quote]
		return image_link

def show_article(request, article_name):
		''' Single Article based on slug '''
		if not article_name == None:
				article_dict = {}
				article = WpPosts.objects.using('wp_crazy').filter(post_name=article_name)
				cats = get_categories(article[0].id)
				break_count = article[0].post_content.count("\n")
				post_content = article[0].post_content.replace("\n", "<br />")
				berta_bridal = make_post_list_by_cat('Berta Bridal')
				boho_style = make_post_list_by_cat('Boho Style')
				claire_petibone = make_post_list_by_cat('Claire Pettibone')
				wedding_hair = make_post_list_by_cat('Wedding Hairstyles', 4)
				hair_count = len(wedding_hair)
				seasonal_notables = make_post_list_by_cat('Winter Weddings', 4)
				context = {'post_content': post_content, 'post': article, 'categories': cats, 'breakcount': break_count, 'berta_bridal': berta_bridal, 'wedding_hair': wedding_hair, 'seasonal_weddings': seasonal_notables, 'boho_style': boho_style, 'claire_petibone': claire_petibone}
				return render(request, 'aggregator/home/article_extended.html', context)
		else:
				pass
		return HttpResponseRedirect('/')

def category_view(request, category=None):
		if category:
				cat_list = make_post_list_by_cat(category, length=100)
				for cat in cat_list:
						pass	
				wedding_hair = make_post_list_by_cat('Wedding Hairstyles', 4)
				seasonal_notables = make_post_list_by_cat('Winter Weddings', 4)
				photo_ideas = make_post_list_by_cat('PHOTO IDEAS', 4)
				centerpieces = make_post_list_by_cat('Centerpieces &amp; Tablescapes', 4)
				content = {'articles': cat_list, 'photo_ideas': photo_ideas, 'centerpieces': centerpieces, 'seasonal_weddings': seasonal_notables, 'wedding_hair': wedding_hair[:4]}
				return render(request, 'aggregator/home/category_results.html', content)
		return render(request, 'aggregator/home/category_results.html')

def search_view(request, search_term=None):
		if request.method == 'POST':
				search_term = request.POST['search_term']
		if search_term:
				#articles = WpPosts.objects.using('wp_crazy').filter(post_title__search=search_term).filter(post_content__search=search_term).filter(post_parent=0).filter(post_type='post').filter(post_status='publish').exclude(post_title='Auto Draft')[:20]
				conn = mdb.connect('localhost', 'root', 'helium', 'wordpress_crazyforus')
				cur = conn.cursor(mdb.cursors.DictCursor)
				cur.execute("SELECT *, MATCH(post_title, post_content) AGAINST('+%s' IN BOOLEAN MODE) AS relevance from `wp_posts` WHERE post_parent = 0 and post_type='post' and post_status='publish' and MATCH(post_title, post_content) AGAINST('+%s' IN BOOLEAN MODE) ORDER BY relevance DESC" % (search_term, search_term))
				rowcount = cur.rowcount
				articles = cur.fetchall()[:30]
				cat_list = set_all_categories() #This is the total list of categories
				post_list = []
				for article in articles:
						article_dict = {}
						article_dict['id'] = article['ID']
								
						article_dict['title'] = article['post_title'].decode("cp1252")
						article_dict['post_content'] = remove_html(article['post_content'], 200)
						article_dict['post_date'] = article['post_date']
						article_dict['slug'] = slugify(article['post_name'])
						article_dict['images'] = get_post_images(article['ID'])
						article_dict['categories'] = get_categories(article['ID'], cat_list)
						article_dict['featured_image'] = get_featured(article['ID'])
						post_list.append(article_dict) 
				wedding_hair = make_post_list_by_cat('Wedding Hairstyles', 4)
				seasonal_notables = make_post_list_by_cat('Winter Weddings', 4)
				photo_ideas = make_post_list_by_cat('PHOTO IDEAS', 4)
				centerpieces = make_post_list_by_cat('Centerpieces &amp; Tablescapes', 4)
				content = {'articles': post_list, 'rowcount': rowcount, 'photo_ideas': photo_ideas, 'centerpieces': centerpieces, 'seasonal_weddings': seasonal_notables, 'wedding_hair': wedding_hair[:4]}
				return render(request, 'aggregator/home/category_results.html', content)
		return render(request, 'aggregator/home/category_results.html')
						
def add_view_count(postid):
		''' If views have been recorded update the row by adding one to the meta value
			if not then create the row and set the meta value to 1 '''
		obj, created = WpPostmeta.get_or_create(post_id=postid)
				

# =================== Strip HTML tags ==================================
def remove_html(html_file, length):
		html_file = html_file[:6000]
		limit = html_file.count("<")
		for i in range(1,limit):
				start = html_file.find("<")
				end = html_file.find(">")
				if end > 0:
						end = end+1
						slice_len = (end-start)
						repl_str = html_file[start:end]
						html_file = html_file[:start] + html_file[end:]
						html_file = html_file.replace("\r", "")
						html_file = html_file.replace("\n", "")
				else:
						break
		html_file=html_file[:length]
		return html_file

# ================== GET Articles by Category ==========================
def make_post_list_by_cat(catname, length=4):
		''' This def will return a dict of articles with the category requested
			This should in the future be able to take multiple categories and return
			articles that cross categorize '''
		cat_post_list = []
		cat_list = set_all_categories() #This is the total list of categories
		postbycat_list = get_posts_by_cat(catname, length)
		if postbycat_list:
				for postid in postbycat_list:
						try:
								article = WpPosts.objects.using('wp_crazy').get(pk=postid)
								article_dict = {}
								article_dict['id'] = article.id
								article_dict['title'] = article.post_title
								article_dict['post_content'] = remove_html(article.post_content, 200)
								article_dict['post_date'] = article.post_date
								article_dict['slug'] = slugify(article.post_name)
								article_dict['images'] = get_post_images(article.id)
								article_dict['categories'] = get_categories(article.id, cat_list)
								article_dict['featured_image'] = get_featured(article.id)
								cat_post_list.append(article_dict)
						except:
								pass
				return cat_post_list
		return "None"

def get_posts_by_cat(catname=None, length=4):
		categories = WpTerms.objects.using('wp_crazy').filter(name=catname)
		if categories:
				postbycat_list = []		
				for category in categories:
						tax_term_id = WpTermTaxonomy.objects.using('wp_crazy').filter(term_id=category.term_id)
						postlist = WpTermRelationships.objects.using('wp_crazy').filter(term_taxonomy_id=tax_term_id[0].term_taxonomy_id).order_by('-object_id')[:length]
						for post in postlist:
								postbycat_list.append(post.object_id)
				return postbycat_list
		return False



		
