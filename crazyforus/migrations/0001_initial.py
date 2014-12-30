# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ArticleAds'
        db.create_table('article_ads', (
            ('article_ads_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('article_code', self.gf('django.db.models.fields.CharField')(max_length=1024L)),
            ('ad_manufacturer', self.gf('django.db.models.fields.CharField')(max_length=128L)),
            ('created_at', self.gf('django.db.models.fields.DateField')()),
            ('last_updated', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'crazyforus', ['ArticleAds'])

        # Adding model 'Articles'
        db.create_table('articles', (
            ('articlesid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=140L)),
            ('datecreated', self.gf('django.db.models.fields.DateField')()),
            ('datepublish', self.gf('django.db.models.fields.DateField')()),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
            ('publish', self.gf('django.db.models.fields.IntegerField')()),
            ('articletype', self.gf('django.db.models.fields.CharField')(max_length=2L, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=60L, blank=True)),
            ('posttext', self.gf('django.db.models.fields.TextField')()),
            ('snippet', self.gf('django.db.models.fields.CharField')(max_length=1024L)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=70L, blank=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=201L, blank=True)),
        ))
        db.send_create_signal(u'crazyforus', ['Articles'])

        # Adding model 'ArticlesImages'
        db.create_table('articles_images', (
            ('articles_images_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('articles_id', self.gf('django.db.models.fields.IntegerField')()),
            ('imagesname', self.gf('django.db.models.fields.CharField')(max_length=128L)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('width', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=512L)),
        ))
        db.send_create_signal(u'crazyforus', ['ArticlesImages'])

        # Adding model 'ArticlesVendors'
        db.create_table('articles_vendors', (
            ('articles_vendors_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('articles_id', self.gf('django.db.models.fields.IntegerField')()),
            ('vendorname', self.gf('django.db.models.fields.CharField')(max_length=100L)),
            ('vendorlink', self.gf('django.db.models.fields.CharField')(max_length=100L)),
            ('vendordesc', self.gf('django.db.models.fields.CharField')(max_length=100L)),
        ))
        db.send_create_signal(u'crazyforus', ['ArticlesVendors'])

        # Adding model 'Directions'
        db.create_table('directions', (
            ('directionsid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('membersid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crazyforus.Members'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=1000L)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=150L)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=7L)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
            ('venue', self.gf('django.db.models.fields.CharField')(max_length=150L)),
        ))
        db.send_create_signal(u'crazyforus', ['Directions'])

        # Adding model 'Emaillist'
        db.create_table('emaillist', (
            ('emaillistid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
            ('exclusive', self.gf('django.db.models.fields.IntegerField')()),
            ('gfirstname', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
            ('glastname', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=150L, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
        ))
        db.send_create_signal(u'crazyforus', ['Emaillist'])

        # Adding model 'Eventlist'
        db.create_table('eventlist', (
            ('eventlistid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('startdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('enddate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('eventtime', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000L, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'crazyforus', ['Eventlist'])

        # Adding model 'Events'
        db.create_table('events', (
            ('eventsid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('membersid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crazyforus.Members'])),
            ('ename', self.gf('django.db.models.fields.CharField')(max_length=150L)),
            ('edate', self.gf('django.db.models.fields.DateField')()),
            ('etime', self.gf('django.db.models.fields.CharField')(max_length=150L, blank=True)),
            ('elocation', self.gf('django.db.models.fields.CharField')(max_length=150L, blank=True)),
            ('eaddress', self.gf('django.db.models.fields.CharField')(max_length=150L, blank=True)),
            ('ecity', self.gf('django.db.models.fields.CharField')(max_length=150L, blank=True)),
            ('estate', self.gf('django.db.models.fields.CharField')(max_length=30L, blank=True)),
            ('ezip', self.gf('django.db.models.fields.CharField')(max_length=9L, blank=True)),
            ('ephone', self.gf('django.db.models.fields.CharField')(max_length=15L, blank=True)),
            ('edescription', self.gf('django.db.models.fields.CharField')(max_length=500L)),
        ))
        db.send_create_signal(u'crazyforus', ['Events'])

        # Adding model 'Family'
        db.create_table('family', (
            ('familyid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('membersid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crazyforus.Members'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80L)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=5000L)),
            ('imagename', self.gf('django.db.models.fields.CharField')(max_length=200L)),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'crazyforus', ['Family'])

        # Adding model 'Fromoutoftown'
        db.create_table('fromoutoftown', (
            ('fromoutoftownid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('membersid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crazyforus.Members'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150L, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=150L, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30L)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=30L)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=500L, blank=True)),
            ('linkname', self.gf('django.db.models.fields.CharField')(max_length=150L, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=150L, blank=True)),
            ('imagename', self.gf('django.db.models.fields.CharField')(max_length=150L, blank=True)),
        ))
        db.send_create_signal(u'crazyforus', ['Fromoutoftown'])

        # Adding model 'Fromus'
        db.create_table('fromus', (
            ('fromusid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=5000L)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('membersid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crazyforus.Members'])),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'crazyforus', ['Fromus'])

        # Adding model 'GownsGallery'
        db.create_table('gowns-gallery', (
            ('gowns_galleryid', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='gowns-galleryid')),
            ('productid', self.gf('django.db.models.fields.CharField')(max_length=11L)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=70L)),
            ('merchantid', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('merchant', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=200L)),
            ('thumbnail', self.gf('django.db.models.fields.CharField')(max_length=200L)),
            ('bigimage', self.gf('django.db.models.fields.CharField')(max_length=200L)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('retailprice', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=70L)),
            ('subcategory', self.gf('django.db.models.fields.CharField')(max_length=70L)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=70L)),
            ('custom1', self.gf('django.db.models.fields.CharField')(max_length=70L)),
            ('custom2', self.gf('django.db.models.fields.CharField')(max_length=70L)),
            ('custom3', self.gf('django.db.models.fields.CharField')(max_length=70L)),
            ('custom4', self.gf('django.db.models.fields.CharField')(max_length=70L)),
            ('custom5', self.gf('django.db.models.fields.CharField')(max_length=70L)),
            ('lastupdated', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=70L)),
            ('partnumber', self.gf('django.db.models.fields.CharField')(max_length=30L)),
            ('merchantcategory', self.gf('django.db.models.fields.CharField')(max_length=70L)),
            ('merchantsubcategory', self.gf('django.db.models.fields.CharField')(max_length=70L)),
            ('shortdescription', self.gf('django.db.models.fields.CharField')(max_length=40L)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=40L)),
        ))
        db.send_create_signal(u'crazyforus', ['GownsGallery'])

        # Adding model 'Guestbook'
        db.create_table('guestbook', (
            ('guestbookid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('membersid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crazyforus.Members'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=5000L)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=150L)),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'crazyforus', ['Guestbook'])

        # Adding model 'Imagecat'
        db.create_table('imagecat', (
            ('imagecatid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('membersid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crazyforus.Members'])),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=300L, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('blurb', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'crazyforus', ['Imagecat'])

        # Adding model 'Imagegal'
        db.create_table('imagegal', (
            ('imagegalid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('imagecatid', self.gf('django.db.models.fields.IntegerField')()),
            ('membersid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crazyforus.Members'])),
            ('imagename', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000L, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'crazyforus', ['Imagegal'])

        # Adding model 'InvitationsWpd'
        db.create_table('invitations_wpd', (
            ('invitations_wpdid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('productid', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('productname', self.gf('django.db.models.fields.CharField')(max_length=75L)),
            ('merchantid', self.gf('django.db.models.fields.CharField')(max_length=15L)),
            ('merchant', self.gf('django.db.models.fields.CharField')(max_length=30L)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=150L)),
            ('thumbnail', self.gf('django.db.models.fields.CharField')(max_length=150L)),
            ('bigimage', self.gf('django.db.models.fields.CharField')(max_length=150L)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=5L)),
            ('retail_price', self.gf('django.db.models.fields.CharField')(max_length=5L)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=40L)),
            ('subcategory', self.gf('django.db.models.fields.CharField')(max_length=40L)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000L)),
            ('custom1', self.gf('django.db.models.fields.CharField')(max_length=75L)),
            ('custom2', self.gf('django.db.models.fields.CharField')(max_length=75L)),
            ('custom3', self.gf('django.db.models.fields.CharField')(max_length=75L)),
            ('custom4', self.gf('django.db.models.fields.CharField')(max_length=75L)),
            ('custom5', self.gf('django.db.models.fields.CharField')(max_length=75L)),
            ('last_updated', self.gf('django.db.models.fields.CharField')(max_length=30L)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=100L)),
            ('merchantcategory', self.gf('django.db.models.fields.CharField')(max_length=75L)),
        ))
        db.send_create_signal(u'crazyforus', ['InvitationsWpd'])

        # Adding model 'Lines'
        db.create_table('lines', (
            ('linesid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('line', self.gf('django.db.models.fields.CharField')(max_length=150L)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=5000L)),
        ))
        db.send_create_signal(u'crazyforus', ['Lines'])

        # Adding model 'Mailinglist'
        db.create_table('mailinglist', (
            ('mailinglistid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('membersid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crazyforus.Members'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60L, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50L, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=10L, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('partyname', self.gf('django.db.models.fields.CharField')(max_length=150L, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15L, blank=True)),
            ('rsvpceremony', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rsvpreception', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rsvpmeal', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'crazyforus', ['Mailinglist'])

        # Adding model 'Members'
        db.create_table('members', (
            ('membersid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=150L, blank=True)),
            ('websitename', self.gf('django.db.models.fields.CharField')(max_length=50L, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=50L, blank=True)),
            ('gfirst_name', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('glast_name', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('bfirst_name', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('blast_name', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30L, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=30L, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=30L, blank=True)),
            ('wedding_date', self.gf('django.db.models.fields.DateField')()),
            ('mainimage', self.gf('django.db.models.fields.CharField')(max_length=150L, blank=True)),
            ('mainimagew', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('mainimageh', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
            ('photogallery', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('template', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('returnnum', self.gf('django.db.models.fields.IntegerField')()),
            ('stepprocess', self.gf('django.db.models.fields.IntegerField')()),
            ('viewable', self.gf('django.db.models.fields.IntegerField')()),
            ('newsletter', self.gf('django.db.models.fields.IntegerField')()),
            ('emailnum', self.gf('django.db.models.fields.IntegerField')()),
            ('emailopen', self.gf('django.db.models.fields.IntegerField')()),
            ('emailopen_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'crazyforus', ['Members'])

        # Adding model 'Newsletter'
        db.create_table('newsletter', (
            ('newsletterid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=150L)),
            ('fname', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('lname', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'crazyforus', ['Newsletter'])

        # Adding model 'NewsletterInfo'
        db.create_table('newsletter_info', (
            ('newsletter_infoid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('imagename', self.gf('django.db.models.fields.CharField')(max_length=150L)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=70L)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=5000L)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=70L)),
        ))
        db.send_create_signal(u'crazyforus', ['NewsletterInfo'])

        # Adding model 'Ourstories'
        db.create_table('ourstories', (
            ('ourstoriesid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('membersid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crazyforus.Members'])),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=6L)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=6000L, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'crazyforus', ['Ourstories'])

        # Adding model 'PostComments'
        db.create_table('post_comments', (
            ('post_comments_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('posts_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=2000L)),
            ('enabled', self.gf('django.db.models.fields.IntegerField')()),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'crazyforus', ['PostComments'])

        # Adding model 'Posts'
        db.create_table('posts', (
            ('posts_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('post_text', self.gf('django.db.models.fields.CharField')(max_length=1000L)),
            ('post_title', self.gf('django.db.models.fields.CharField')(max_length=300L)),
            ('enabled', self.gf('django.db.models.fields.IntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'crazyforus', ['Posts'])

        # Adding model 'PostsImages'
        db.create_table('posts_images', (
            ('posts_images_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('posts_id', self.gf('django.db.models.fields.IntegerField')()),
            ('imagename', self.gf('django.db.models.fields.CharField')(max_length=128L)),
            ('image_text', self.gf('django.db.models.fields.CharField')(max_length=256L)),
            ('orig_width', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('orig_height', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'crazyforus', ['PostsImages'])

        # Adding model 'Quoterequest'
        db.create_table('quoterequest', (
            ('quoterequestid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40L)),
            ('eventdate', self.gf('django.db.models.fields.CharField')(max_length=30L)),
            ('numpeople', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('estbudget', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=150L)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=600L)),
            ('service_cat', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=75L)),
            ('email_verification', self.gf('django.db.models.fields.CharField')(max_length=75L)),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('email_sent', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'crazyforus', ['Quoterequest'])

        # Adding model 'Quoteresponse'
        db.create_table('quoteresponse', (
            ('quoteresponseid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('quoterequestid', self.gf('django.db.models.fields.IntegerField')()),
            ('vendorsid', self.gf('django.db.models.fields.IntegerField')()),
            ('response', self.gf('django.db.models.fields.CharField')(max_length=1000L)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('email_verification', self.gf('django.db.models.fields.CharField')(max_length=75L)),
            ('email_open', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'crazyforus', ['Quoteresponse'])

        # Adding model 'Registry'
        db.create_table('registry', (
            ('registryid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('membersid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crazyforus.Members'])),
            ('storename', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('names', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15L)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=150L)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=5L)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=150L)),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'crazyforus', ['Registry'])

        # Adding model 'Rsvp'
        db.create_table('rsvp', (
            ('rsvpid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('membersid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crazyforus.Members'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40L, blank=True)),
            ('mainquestion', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('maxattend', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('meal', self.gf('django.db.models.fields.CharField')(max_length=500L, blank=True)),
            ('imagename', self.gf('django.db.models.fields.CharField')(max_length=150L, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'crazyforus', ['Rsvp'])

        # Adding model 'Rsvpguests'
        db.create_table('rsvpguests', (
            ('rsvpguestsid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('membersid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crazyforus.Members'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('attending', self.gf('django.db.models.fields.IntegerField')()),
            ('meals', self.gf('django.db.models.fields.CharField')(max_length=500L)),
            ('specialreq', self.gf('django.db.models.fields.CharField')(max_length=1000L)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=150L)),
        ))
        db.send_create_signal(u'crazyforus', ['Rsvpguests'])

        # Adding model 'Sitenav'
        db.create_table('sitenav', (
            ('sitenavid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('membersid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crazyforus.Members'])),
            ('welcome', self.gf('django.db.models.fields.CharField')(max_length=45L)),
            ('fromus', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('ourstories', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('weddingparty', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('ourevents', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('registry', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('wishlist', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('photos', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('fromoutoftown', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('rsvp', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('guestbook', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('extrainfo', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('directions', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('webmedia', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('mailinglist', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('family', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('honeymoon', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('contactus', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('newsletter', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('a_welcome', self.gf('django.db.models.fields.IntegerField')()),
            ('a_fromus', self.gf('django.db.models.fields.IntegerField')()),
            ('a_ourstories', self.gf('django.db.models.fields.IntegerField')()),
            ('a_weddingparty', self.gf('django.db.models.fields.IntegerField')()),
            ('a_ourevents', self.gf('django.db.models.fields.IntegerField')()),
            ('a_guestbook', self.gf('django.db.models.fields.IntegerField')()),
            ('a_registry', self.gf('django.db.models.fields.IntegerField')()),
            ('a_wishlist', self.gf('django.db.models.fields.IntegerField')()),
            ('a_photos', self.gf('django.db.models.fields.IntegerField')()),
            ('a_fromoutoftown', self.gf('django.db.models.fields.IntegerField')()),
            ('a_rsvp', self.gf('django.db.models.fields.IntegerField')()),
            ('a_newsletter', self.gf('django.db.models.fields.IntegerField')()),
            ('a_extrainfo', self.gf('django.db.models.fields.IntegerField')()),
            ('a_directions', self.gf('django.db.models.fields.IntegerField')()),
            ('a_webmedia', self.gf('django.db.models.fields.IntegerField')()),
            ('a_mailinglist', self.gf('django.db.models.fields.IntegerField')()),
            ('a_family', self.gf('django.db.models.fields.IntegerField')()),
            ('a_honeymoon', self.gf('django.db.models.fields.IntegerField')()),
            ('a_contactus', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'crazyforus', ['Sitenav'])

        # Adding model 'Tasklist'
        db.create_table('tasklist', (
            ('tasklistid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200L)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000L, blank=True)),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=45L)),
        ))
        db.send_create_signal(u'crazyforus', ['Tasklist'])

        # Adding model 'Vendors'
        db.create_table('vendors', (
            ('vendorsid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('vendorname', self.gf('django.db.models.fields.CharField')(max_length=70L)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('service', self.gf('django.db.models.fields.CharField')(max_length=40L, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=40L, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=25L, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')()),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=17L, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=15L, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=5000L, blank=True)),
            ('addedby', self.gf('django.db.models.fields.CharField')(max_length=15L)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('logo', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('package', self.gf('django.db.models.fields.IntegerField')()),
            ('portfolio1', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('portfolio2', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('portfolio3', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('portfolio4', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('portfolio5', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=50L, blank=True)),
            ('returnnum', self.gf('django.db.models.fields.IntegerField')()),
            ('featureimage', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('portfoliodesc1', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('portfoliodesc2', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('portfoliodesc3', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('portfoliodesc4', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('portfoliodesc5', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('bannerimage', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('emailaction', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=5000L, blank=True)),
            ('pagecount', self.gf('django.db.models.fields.IntegerField')()),
            ('sitecount', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('websitecnt', self.gf('django.db.models.fields.IntegerField')()),
            ('trial_period', self.gf('django.db.models.fields.IntegerField')()),
            ('trial_start_date', self.gf('django.db.models.fields.DateField')()),
            ('offer_end_date', self.gf('django.db.models.fields.CharField')(max_length=30L)),
            ('newsletter', self.gf('django.db.models.fields.IntegerField')()),
            ('quote_option', self.gf('django.db.models.fields.IntegerField')()),
            ('emailnum', self.gf('django.db.models.fields.IntegerField')()),
            ('emailopen', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'crazyforus', ['Vendors'])

        # Adding model 'VendorsAddcontact'
        db.create_table('vendors_addcontact', (
            ('vendors_addcontactid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('vendorsid', self.gf('django.db.models.fields.IntegerField')()),
            ('acctmgr', self.gf('django.db.models.fields.CharField')(max_length=75L)),
            ('rating', self.gf('django.db.models.fields.CharField')(max_length=30L, blank=True)),
            ('inbridalshow', self.gf('django.db.models.fields.CharField')(max_length=30L, blank=True)),
            ('reciprocal', self.gf('django.db.models.fields.CharField')(max_length=10L, blank=True)),
            ('monthlyadbudget', self.gf('django.db.models.fields.CharField')(max_length=15L, blank=True)),
            ('notamember', self.gf('django.db.models.fields.CharField')(max_length=30L, blank=True)),
        ))
        db.send_create_signal(u'crazyforus', ['VendorsAddcontact'])

        # Adding model 'VendorsContacts'
        db.create_table('vendors_contacts', (
            ('vendors_contactsid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('vendorsid', self.gf('django.db.models.fields.IntegerField')()),
            ('prefix', self.gf('django.db.models.fields.CharField')(max_length=5L, blank=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=20L, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=150L, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500L, blank=True)),
        ))
        db.send_create_signal(u'crazyforus', ['VendorsContacts'])

        # Adding model 'VendorsSitecount'
        db.create_table('vendors_sitecount', (
            ('vendors_sitecount', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('vendorid', self.gf('django.db.models.fields.IntegerField')()),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('referrer', self.gf('django.db.models.fields.CharField')(max_length=200L)),
            ('userip', self.gf('django.db.models.fields.CharField')(max_length=30L)),
            ('user_agent', self.gf('django.db.models.fields.CharField')(max_length=200L)),
            ('linktype', self.gf('django.db.models.fields.CharField')(max_length=15L)),
            ('page', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'crazyforus', ['VendorsSitecount'])

        # Adding model 'Weddingparty'
        db.create_table('weddingparty', (
            ('weddingpartyid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('membersid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crazyforus.Members'])),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=5000L)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40L)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40L)),
            ('imagename', self.gf('django.db.models.fields.CharField')(max_length=200L)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'crazyforus', ['Weddingparty'])

        # Adding model 'Welcome'
        db.create_table('welcome', (
            ('welcomeid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('membersid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crazyforus.Members'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50L, blank=True)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=3000L, blank=True)),
            ('mainimage', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'crazyforus', ['Welcome'])

        # Adding model 'Wishlist'
        db.create_table('wishlist', (
            ('wishlistid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('membersid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crazyforus.Members'])),
            ('wishname', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('names', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15L)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=150L)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=30L)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=12L)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=150L)),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'crazyforus', ['Wishlist'])

        # Adding model 'Zipcode'
        db.create_table('zipcode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')()),
            ('stateabbr', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=28L)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=30L)),
        ))
        db.send_create_signal(u'crazyforus', ['Zipcode'])


    def backwards(self, orm):
        # Deleting model 'ArticleAds'
        db.delete_table('article_ads')

        # Deleting model 'Articles'
        db.delete_table('articles')

        # Deleting model 'ArticlesImages'
        db.delete_table('articles_images')

        # Deleting model 'ArticlesVendors'
        db.delete_table('articles_vendors')

        # Deleting model 'Directions'
        db.delete_table('directions')

        # Deleting model 'Emaillist'
        db.delete_table('emaillist')

        # Deleting model 'Eventlist'
        db.delete_table('eventlist')

        # Deleting model 'Events'
        db.delete_table('events')

        # Deleting model 'Family'
        db.delete_table('family')

        # Deleting model 'Fromoutoftown'
        db.delete_table('fromoutoftown')

        # Deleting model 'Fromus'
        db.delete_table('fromus')

        # Deleting model 'GownsGallery'
        db.delete_table('gowns-gallery')

        # Deleting model 'Guestbook'
        db.delete_table('guestbook')

        # Deleting model 'Imagecat'
        db.delete_table('imagecat')

        # Deleting model 'Imagegal'
        db.delete_table('imagegal')

        # Deleting model 'InvitationsWpd'
        db.delete_table('invitations_wpd')

        # Deleting model 'Lines'
        db.delete_table('lines')

        # Deleting model 'Mailinglist'
        db.delete_table('mailinglist')

        # Deleting model 'Members'
        db.delete_table('members')

        # Deleting model 'Newsletter'
        db.delete_table('newsletter')

        # Deleting model 'NewsletterInfo'
        db.delete_table('newsletter_info')

        # Deleting model 'Ourstories'
        db.delete_table('ourstories')

        # Deleting model 'PostComments'
        db.delete_table('post_comments')

        # Deleting model 'Posts'
        db.delete_table('posts')

        # Deleting model 'PostsImages'
        db.delete_table('posts_images')

        # Deleting model 'Quoterequest'
        db.delete_table('quoterequest')

        # Deleting model 'Quoteresponse'
        db.delete_table('quoteresponse')

        # Deleting model 'Registry'
        db.delete_table('registry')

        # Deleting model 'Rsvp'
        db.delete_table('rsvp')

        # Deleting model 'Rsvpguests'
        db.delete_table('rsvpguests')

        # Deleting model 'Sitenav'
        db.delete_table('sitenav')

        # Deleting model 'Tasklist'
        db.delete_table('tasklist')

        # Deleting model 'Vendors'
        db.delete_table('vendors')

        # Deleting model 'VendorsAddcontact'
        db.delete_table('vendors_addcontact')

        # Deleting model 'VendorsContacts'
        db.delete_table('vendors_contacts')

        # Deleting model 'VendorsSitecount'
        db.delete_table('vendors_sitecount')

        # Deleting model 'Weddingparty'
        db.delete_table('weddingparty')

        # Deleting model 'Welcome'
        db.delete_table('welcome')

        # Deleting model 'Wishlist'
        db.delete_table('wishlist')

        # Deleting model 'Zipcode'
        db.delete_table('zipcode')


    models = {
        u'crazyforus.articleads': {
            'Meta': {'object_name': 'ArticleAds', 'db_table': "'article_ads'"},
            'ad_manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '128L'}),
            'article_ads_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'article_code': ('django.db.models.fields.CharField', [], {'max_length': '1024L'}),
            'created_at': ('django.db.models.fields.DateField', [], {}),
            'last_updated': ('django.db.models.fields.DateField', [], {})
        },
        u'crazyforus.articles': {
            'Meta': {'object_name': 'Articles', 'db_table': "'articles'"},
            'articlesid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'articletype': ('django.db.models.fields.CharField', [], {'max_length': '2L', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '60L', 'blank': 'True'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'}),
            'datecreated': ('django.db.models.fields.DateField', [], {}),
            'datepublish': ('django.db.models.fields.DateField', [], {}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '70L', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '201L', 'blank': 'True'}),
            'posttext': ('django.db.models.fields.TextField', [], {}),
            'publish': ('django.db.models.fields.IntegerField', [], {}),
            'snippet': ('django.db.models.fields.CharField', [], {'max_length': '1024L'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140L'})
        },
        u'crazyforus.articlesimages': {
            'Meta': {'object_name': 'ArticlesImages', 'db_table': "'articles_images'"},
            'articles_id': ('django.db.models.fields.IntegerField', [], {}),
            'articles_images_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '512L'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'imagesname': ('django.db.models.fields.CharField', [], {'max_length': '128L'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'width': ('django.db.models.fields.CharField', [], {'max_length': '10L'})
        },
        u'crazyforus.articlesvendors': {
            'Meta': {'object_name': 'ArticlesVendors', 'db_table': "'articles_vendors'"},
            'articles_id': ('django.db.models.fields.IntegerField', [], {}),
            'articles_vendors_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'vendordesc': ('django.db.models.fields.CharField', [], {'max_length': '100L'}),
            'vendorlink': ('django.db.models.fields.CharField', [], {'max_length': '100L'}),
            'vendorname': ('django.db.models.fields.CharField', [], {'max_length': '100L'})
        },
        u'crazyforus.directions': {
            'Meta': {'object_name': 'Directions', 'db_table': "'directions'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150L'}),
            'body': ('django.db.models.fields.CharField', [], {'max_length': '1000L'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'directionsid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'membersid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crazyforus.Members']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'venue': ('django.db.models.fields.CharField', [], {'max_length': '150L'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '7L'})
        },
        u'crazyforus.emaillist': {
            'Meta': {'object_name': 'Emaillist', 'db_table': "'emaillist'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'}),
            'emaillistid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'exclusive': ('django.db.models.fields.IntegerField', [], {}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'}),
            'gfirstname': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'}),
            'glastname': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'})
        },
        u'crazyforus.eventlist': {
            'Meta': {'object_name': 'Eventlist', 'db_table': "'eventlist'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000L', 'blank': 'True'}),
            'enddate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'eventlistid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'eventtime': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'startdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'crazyforus.events': {
            'Meta': {'object_name': 'Events', 'db_table': "'events'"},
            'eaddress': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'ecity': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'edate': ('django.db.models.fields.DateField', [], {}),
            'edescription': ('django.db.models.fields.CharField', [], {'max_length': '500L'}),
            'elocation': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'ename': ('django.db.models.fields.CharField', [], {'max_length': '150L'}),
            'ephone': ('django.db.models.fields.CharField', [], {'max_length': '15L', 'blank': 'True'}),
            'estate': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'blank': 'True'}),
            'etime': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'eventsid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'ezip': ('django.db.models.fields.CharField', [], {'max_length': '9L', 'blank': 'True'}),
            'membersid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crazyforus.Members']"})
        },
        u'crazyforus.family': {
            'Meta': {'object_name': 'Family', 'db_table': "'family'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'body': ('django.db.models.fields.CharField', [], {'max_length': '5000L'}),
            'familyid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'imagename': ('django.db.models.fields.CharField', [], {'max_length': '200L'}),
            'membersid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crazyforus.Members']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80L'})
        },
        u'crazyforus.fromoutoftown': {
            'Meta': {'object_name': 'Fromoutoftown', 'db_table': "'fromoutoftown'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30L'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '500L', 'blank': 'True'}),
            'fromoutoftownid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'imagename': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'linkname': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'membersid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crazyforus.Members']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30L'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'})
        },
        u'crazyforus.fromus': {
            'Meta': {'object_name': 'Fromus', 'db_table': "'fromus'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'body': ('django.db.models.fields.CharField', [], {'max_length': '5000L'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'fromusid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'membersid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crazyforus.Members']"})
        },
        u'crazyforus.gownsgallery': {
            'Meta': {'object_name': 'GownsGallery', 'db_table': "'gowns-gallery'"},
            'bigimage': ('django.db.models.fields.CharField', [], {'max_length': '200L'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '70L'}),
            'custom1': ('django.db.models.fields.CharField', [], {'max_length': '70L'}),
            'custom2': ('django.db.models.fields.CharField', [], {'max_length': '70L'}),
            'custom3': ('django.db.models.fields.CharField', [], {'max_length': '70L'}),
            'custom4': ('django.db.models.fields.CharField', [], {'max_length': '70L'}),
            'custom5': ('django.db.models.fields.CharField', [], {'max_length': '70L'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '70L'}),
            'gowns_galleryid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'gowns-galleryid'"}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '40L'}),
            'lastupdated': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200L'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '70L'}),
            'merchant': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'merchantcategory': ('django.db.models.fields.CharField', [], {'max_length': '70L'}),
            'merchantid': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'merchantsubcategory': ('django.db.models.fields.CharField', [], {'max_length': '70L'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70L'}),
            'partnumber': ('django.db.models.fields.CharField', [], {'max_length': '30L'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'productid': ('django.db.models.fields.CharField', [], {'max_length': '11L'}),
            'retailprice': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'shortdescription': ('django.db.models.fields.CharField', [], {'max_length': '40L'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'subcategory': ('django.db.models.fields.CharField', [], {'max_length': '70L'}),
            'thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '200L'})
        },
        u'crazyforus.guestbook': {
            'Meta': {'object_name': 'Guestbook', 'db_table': "'guestbook'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '5000L'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '150L'}),
            'guestbookid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'membersid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crazyforus.Members']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50L'})
        },
        u'crazyforus.imagecat': {
            'Meta': {'object_name': 'Imagecat', 'db_table': "'imagecat'"},
            'blurb': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '300L', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'imagecatid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'membersid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crazyforus.Members']"})
        },
        u'crazyforus.imagegal': {
            'Meta': {'object_name': 'Imagegal', 'db_table': "'imagegal'"},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000L', 'blank': 'True'}),
            'imagecatid': ('django.db.models.fields.IntegerField', [], {}),
            'imagegalid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'imagename': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'membersid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crazyforus.Members']"})
        },
        u'crazyforus.invitationswpd': {
            'Meta': {'object_name': 'InvitationsWpd', 'db_table': "'invitations_wpd'"},
            'bigimage': ('django.db.models.fields.CharField', [], {'max_length': '150L'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '40L'}),
            'custom1': ('django.db.models.fields.CharField', [], {'max_length': '75L'}),
            'custom2': ('django.db.models.fields.CharField', [], {'max_length': '75L'}),
            'custom3': ('django.db.models.fields.CharField', [], {'max_length': '75L'}),
            'custom4': ('django.db.models.fields.CharField', [], {'max_length': '75L'}),
            'custom5': ('django.db.models.fields.CharField', [], {'max_length': '75L'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000L'}),
            'invitations_wpdid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.CharField', [], {'max_length': '30L'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '150L'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '100L'}),
            'merchant': ('django.db.models.fields.CharField', [], {'max_length': '30L'}),
            'merchantcategory': ('django.db.models.fields.CharField', [], {'max_length': '75L'}),
            'merchantid': ('django.db.models.fields.CharField', [], {'max_length': '15L'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '5L'}),
            'productid': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'productname': ('django.db.models.fields.CharField', [], {'max_length': '75L'}),
            'retail_price': ('django.db.models.fields.CharField', [], {'max_length': '5L'}),
            'subcategory': ('django.db.models.fields.CharField', [], {'max_length': '40L'}),
            'thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '150L'})
        },
        u'crazyforus.lines': {
            'Meta': {'object_name': 'Lines', 'db_table': "'lines'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000L'}),
            'line': ('django.db.models.fields.CharField', [], {'max_length': '150L'}),
            'linesid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'crazyforus.mailinglist': {
            'Meta': {'object_name': 'Mailinglist', 'db_table': "'mailinglist'"},
            'active': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'mailinglistid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'membersid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crazyforus.Members']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60L', 'blank': 'True'}),
            'partyname': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15L', 'blank': 'True'}),
            'rsvpceremony': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rsvpmeal': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rsvpreception': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'crazyforus.members': {
            'Meta': {'object_name': 'Members', 'db_table': "'members'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'bfirst_name': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'blast_name': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'emailnum': ('django.db.models.fields.IntegerField', [], {}),
            'emailopen': ('django.db.models.fields.IntegerField', [], {}),
            'emailopen_date': ('django.db.models.fields.DateField', [], {}),
            'gfirst_name': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'glast_name': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'mainimage': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'mainimageh': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mainimagew': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'membersid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'newsletter': ('django.db.models.fields.IntegerField', [], {}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'photogallery': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'returnnum': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'blank': 'True'}),
            'stepprocess': ('django.db.models.fields.IntegerField', [], {}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'viewable': ('django.db.models.fields.IntegerField', [], {}),
            'websitename': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'wedding_date': ('django.db.models.fields.DateField', [], {}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'crazyforus.newsletter': {
            'Meta': {'object_name': 'Newsletter', 'db_table': "'newsletter'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '150L'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'newsletterid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'crazyforus.newsletterinfo': {
            'Meta': {'object_name': 'NewsletterInfo', 'db_table': "'newsletter_info'"},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '5000L'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '70L'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'imagename': ('django.db.models.fields.CharField', [], {'max_length': '150L'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70L'}),
            'newsletter_infoid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'crazyforus.ourstories': {
            'Meta': {'object_name': 'Ourstories', 'db_table': "'ourstories'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'body': ('django.db.models.fields.CharField', [], {'max_length': '6000L', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'membersid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crazyforus.Members']"}),
            'ourstoriesid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '6L'})
        },
        u'crazyforus.postcomments': {
            'Meta': {'object_name': 'PostComments', 'db_table': "'post_comments'"},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '2000L'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'enabled': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'post_comments_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'posts_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'crazyforus.posts': {
            'Meta': {'object_name': 'Posts', 'db_table': "'posts'"},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'enabled': ('django.db.models.fields.IntegerField', [], {}),
            'post_text': ('django.db.models.fields.CharField', [], {'max_length': '1000L'}),
            'post_title': ('django.db.models.fields.CharField', [], {'max_length': '300L'}),
            'posts_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'crazyforus.postsimages': {
            'Meta': {'object_name': 'PostsImages', 'db_table': "'posts_images'"},
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'image_text': ('django.db.models.fields.CharField', [], {'max_length': '256L'}),
            'imagename': ('django.db.models.fields.CharField', [], {'max_length': '128L'}),
            'orig_height': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'orig_width': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'posts_id': ('django.db.models.fields.IntegerField', [], {}),
            'posts_images_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'crazyforus.quoterequest': {
            'Meta': {'object_name': 'Quoterequest', 'db_table': "'quoterequest'"},
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '150L'}),
            'email_sent': ('django.db.models.fields.IntegerField', [], {}),
            'email_verification': ('django.db.models.fields.CharField', [], {'max_length': '75L'}),
            'estbudget': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'eventdate': ('django.db.models.fields.CharField', [], {'max_length': '30L'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '75L'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40L'}),
            'numpeople': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '600L'}),
            'quoterequestid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'service_cat': ('django.db.models.fields.CharField', [], {'max_length': '50L'})
        },
        u'crazyforus.quoteresponse': {
            'Meta': {'object_name': 'Quoteresponse', 'db_table': "'quoteresponse'"},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'email_open': ('django.db.models.fields.IntegerField', [], {}),
            'email_verification': ('django.db.models.fields.CharField', [], {'max_length': '75L'}),
            'quoterequestid': ('django.db.models.fields.IntegerField', [], {}),
            'quoteresponseid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '1000L'}),
            'vendorsid': ('django.db.models.fields.IntegerField', [], {})
        },
        u'crazyforus.registry': {
            'Meta': {'object_name': 'Registry', 'db_table': "'registry'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150L'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '150L'}),
            'membersid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crazyforus.Members']"}),
            'names': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15L'}),
            'registryid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'storename': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5L'})
        },
        u'crazyforus.rsvp': {
            'Meta': {'object_name': 'Rsvp', 'db_table': "'rsvp'"},
            'active': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'imagename': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'mainquestion': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'maxattend': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'meal': ('django.db.models.fields.CharField', [], {'max_length': '500L', 'blank': 'True'}),
            'membersid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crazyforus.Members']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40L', 'blank': 'True'}),
            'rsvpid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'crazyforus.rsvpguests': {
            'Meta': {'object_name': 'Rsvpguests', 'db_table': "'rsvpguests'"},
            'attending': ('django.db.models.fields.IntegerField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '150L'}),
            'meals': ('django.db.models.fields.CharField', [], {'max_length': '500L'}),
            'membersid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crazyforus.Members']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'rsvpguestsid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'specialreq': ('django.db.models.fields.CharField', [], {'max_length': '1000L'})
        },
        u'crazyforus.sitenav': {
            'Meta': {'object_name': 'Sitenav', 'db_table': "'sitenav'"},
            'a_contactus': ('django.db.models.fields.IntegerField', [], {}),
            'a_directions': ('django.db.models.fields.IntegerField', [], {}),
            'a_extrainfo': ('django.db.models.fields.IntegerField', [], {}),
            'a_family': ('django.db.models.fields.IntegerField', [], {}),
            'a_fromoutoftown': ('django.db.models.fields.IntegerField', [], {}),
            'a_fromus': ('django.db.models.fields.IntegerField', [], {}),
            'a_guestbook': ('django.db.models.fields.IntegerField', [], {}),
            'a_honeymoon': ('django.db.models.fields.IntegerField', [], {}),
            'a_mailinglist': ('django.db.models.fields.IntegerField', [], {}),
            'a_newsletter': ('django.db.models.fields.IntegerField', [], {}),
            'a_ourevents': ('django.db.models.fields.IntegerField', [], {}),
            'a_ourstories': ('django.db.models.fields.IntegerField', [], {}),
            'a_photos': ('django.db.models.fields.IntegerField', [], {}),
            'a_registry': ('django.db.models.fields.IntegerField', [], {}),
            'a_rsvp': ('django.db.models.fields.IntegerField', [], {}),
            'a_webmedia': ('django.db.models.fields.IntegerField', [], {}),
            'a_weddingparty': ('django.db.models.fields.IntegerField', [], {}),
            'a_welcome': ('django.db.models.fields.IntegerField', [], {}),
            'a_wishlist': ('django.db.models.fields.IntegerField', [], {}),
            'contactus': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'directions': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'extrainfo': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'family': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'fromoutoftown': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'fromus': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'guestbook': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'honeymoon': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'mailinglist': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'membersid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crazyforus.Members']"}),
            'newsletter': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'ourevents': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'ourstories': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'photos': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'registry': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'rsvp': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'sitenavid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'webmedia': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'weddingparty': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'welcome': ('django.db.models.fields.CharField', [], {'max_length': '45L'}),
            'wishlist': ('django.db.models.fields.CharField', [], {'max_length': '60L'})
        },
        u'crazyforus.tasklist': {
            'Meta': {'object_name': 'Tasklist', 'db_table': "'tasklist'"},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '45L'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000L', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200L'}),
            'position': ('django.db.models.fields.IntegerField', [], {}),
            'tasklistid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'crazyforus.vendors': {
            'Meta': {'object_name': 'Vendors', 'db_table': "'vendors'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'addedby': ('django.db.models.fields.CharField', [], {'max_length': '15L'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'bannerimage': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '40L', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000L', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'emailaction': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'emailnum': ('django.db.models.fields.IntegerField', [], {}),
            'emailopen': ('django.db.models.fields.IntegerField', [], {}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '15L', 'blank': 'True'}),
            'featureimage': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'logo': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'newsletter': ('django.db.models.fields.IntegerField', [], {}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '5000L', 'blank': 'True'}),
            'offer_end_date': ('django.db.models.fields.CharField', [], {'max_length': '30L'}),
            'package': ('django.db.models.fields.IntegerField', [], {}),
            'pagecount': ('django.db.models.fields.IntegerField', [], {}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '17L', 'blank': 'True'}),
            'portfolio1': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'portfolio2': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'portfolio3': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'portfolio4': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'portfolio5': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'portfoliodesc1': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'portfoliodesc2': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'portfoliodesc3': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'portfoliodesc4': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'portfoliodesc5': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'quote_option': ('django.db.models.fields.IntegerField', [], {}),
            'returnnum': ('django.db.models.fields.IntegerField', [], {}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '40L', 'blank': 'True'}),
            'sitecount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '25L', 'blank': 'True'}),
            'trial_period': ('django.db.models.fields.IntegerField', [], {}),
            'trial_start_date': ('django.db.models.fields.DateField', [], {}),
            'vendorname': ('django.db.models.fields.CharField', [], {'max_length': '70L'}),
            'vendorsid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'websitecnt': ('django.db.models.fields.IntegerField', [], {}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {})
        },
        u'crazyforus.vendorsaddcontact': {
            'Meta': {'object_name': 'VendorsAddcontact', 'db_table': "'vendors_addcontact'"},
            'acctmgr': ('django.db.models.fields.CharField', [], {'max_length': '75L'}),
            'inbridalshow': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'blank': 'True'}),
            'monthlyadbudget': ('django.db.models.fields.CharField', [], {'max_length': '15L', 'blank': 'True'}),
            'notamember': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'blank': 'True'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'blank': 'True'}),
            'reciprocal': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'blank': 'True'}),
            'vendors_addcontactid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'vendorsid': ('django.db.models.fields.IntegerField', [], {})
        },
        u'crazyforus.vendorscontacts': {
            'Meta': {'object_name': 'VendorsContacts', 'db_table': "'vendors_contacts'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500L', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'blank': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '5L', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'}),
            'vendors_contactsid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'vendorsid': ('django.db.models.fields.IntegerField', [], {})
        },
        u'crazyforus.vendorssitecount': {
            'Meta': {'object_name': 'VendorsSitecount', 'db_table': "'vendors_sitecount'"},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'linktype': ('django.db.models.fields.CharField', [], {'max_length': '15L'}),
            'page': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'referrer': ('django.db.models.fields.CharField', [], {'max_length': '200L'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '200L'}),
            'userip': ('django.db.models.fields.CharField', [], {'max_length': '30L'}),
            'vendorid': ('django.db.models.fields.IntegerField', [], {}),
            'vendors_sitecount': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10L'})
        },
        u'crazyforus.weddingparty': {
            'Meta': {'object_name': 'Weddingparty', 'db_table': "'weddingparty'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'body': ('django.db.models.fields.CharField', [], {'max_length': '5000L'}),
            'imagename': ('django.db.models.fields.CharField', [], {'max_length': '200L'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'membersid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crazyforus.Members']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40L'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40L'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'weddingpartyid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'crazyforus.welcome': {
            'Meta': {'object_name': 'Welcome', 'db_table': "'welcome'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'body': ('django.db.models.fields.CharField', [], {'max_length': '3000L', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'mainimage': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'membersid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crazyforus.Members']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'welcomeid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'crazyforus.wishlist': {
            'Meta': {'object_name': 'Wishlist', 'db_table': "'wishlist'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150L'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '150L'}),
            'membersid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crazyforus.Members']"}),
            'names': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15L'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30L'}),
            'wishlistid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'wishname': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '12L'})
        },
        u'crazyforus.zipcode': {
            'Meta': {'object_name': 'Zipcode', 'db_table': "'zipcode'"},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '28L'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30L'}),
            'stateabbr': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['crazyforus']