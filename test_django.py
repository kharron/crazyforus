import os, sys
sys.path.append('/www/sites/crazyforus.com')
os.environ['DJANGO_SETTINGS_MODULE'] = 'crazyforus.settings'
from aggregator.models import Articles, Category
from aggregator.wp_models import WpPosts, WpTerms, WpTermTaxonomy, WpTermRelationships, WpPostmeta

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
				image_name = image.post_title + "." + extension
				image_link = "http://www.crazyforus.com/wp-content/uploads/%s/%s/%s" % (p_date[0], p_date[1], image_name)
				image_list.append(image_link)
		return image_list

def get_categories(postid, cat_list):
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

def get_featured(postid, post_date):
		p_date_arr = str(post_date).split(" ")
		p_date = p_date_arr[0]
		p_date = p_date.split("-")
		featured = WpPostmeta.objects.using('wp_crazy').filter(meta_key='_thumbnail_id').filter(post_id=postid)
		if len(featured):
			image_post_id = featured[0].meta_value
			image_row = WpPosts.objects.using('wp_crazy').get(id=image_post_id)
			image_name = image_row.post_title
			image_link = "http://www.crazyforus.com/wp-content/uploads/%s/%s/%s" % (p_date[0], p_date[1], image_name)
			return image_link
		return "None"


cat_list = set_all_categories()
posts = WpPosts.objects.using('wp_crazy').filter(post_parent=0).filter(post_type='post').exclude(post_title='Auto Draft').order_by('-id')[:1]
post_dict = {}
for post in posts:
		post_dict = {}
		post_dict['id'] = post.id
		post_dict['title'] = post.post_title
		post_dict['images'] = get_post_images(post.id)
		post_dict['categories'] = get_categories(post.id, cat_list)
		post_dict['featured_image'] = get_featured(post.id, post.post_date)
		print post_dict['images']
		
print "Done"
