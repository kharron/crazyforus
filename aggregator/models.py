from django.db import models

# Create your models here.
class Articles(models.Model):
		name = models.CharField(max_length=100)
		legacy_postid = models.IntegerField(null=True, blank=True)
		title = models.CharField(max_length=100)
		slug = models.SlugField(null=True, blank=True, max_length=100)
		article_text = models.TextField()
		source_name = models.CharField(max_length=128)
		source_site = models.CharField(max_length=512)
		source_link = models.CharField(max_length=700)
		original_date = models.DateTimeField(null=True, blank=True)
		mainthumb = models.IntegerField(null=True, blank=True)
		publish_datetime = models.DateTimeField(null=True, blank=True)
		times_viewed = models.IntegerField(null=False, default=0)
		created_at = models.DateTimeField(auto_now_add=True)
		updated_at = models.DateTimeField(auto_now=True)

class ArticleImages(models.Model):		
		articles = models.ForeignKey('Articles')
		image_link = models.CharField(max_length=256)
		image_name = models.CharField(max_length=128)
		width = models.IntegerField(null=True, blank=True)
		height = models.IntegerField(null=True, blank=True)
		creator = models.CharField(max_length=128, null=True, blank=True)
		title = models.CharField(max_length=256, null=True, blank=True)
		caption = models.CharField(max_length=512, null=True, blank=True)
		cropped = models.IntegerField(null=False, default=0)
		created_at = models.DateTimeField(auto_now_add=True)
		updated_at = models.DateTimeField(auto_now=True)	

class Tags(models.Model):
		articles = models.ForeignKey('Articles')
		tagname = models.CharField(max_length=50)

#This is essentially a join table
class Categories(models.Model):
		articles = models.ForeignKey('Articles')
		categoryname = models.CharField(max_length=50)

#This is the list of categories
class Category(models.Model):
		name = models.CharField(max_length=60)
