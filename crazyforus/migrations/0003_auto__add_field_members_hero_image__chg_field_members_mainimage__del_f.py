# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Ourstories.members'
        db.add_column('ourstories', 'members',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Members.hero_image'
        db.add_column('members', 'hero_image',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True),
                      keep_default=False)


        # Changing field 'Members.mainimage'
        db.alter_column('members', 'mainimage', self.gf('django.db.models.fields.CharField')(max_length=150L))

        # Changing field 'Members.emailopen_date'
        db.alter_column('members', 'emailopen_date', self.gf('django.db.models.fields.DateField')(null=True))
        # Deleting field 'VendorsAddcontact.reciprocal'
        db.delete_column('vendors_addcontact', 'reciprocal')


    def backwards(self, orm):
        # Deleting field 'Ourstories.members'
        db.delete_column('ourstories', 'members')

        # Deleting field 'Members.hero_image'
        db.delete_column('members', 'hero_image')


        # Changing field 'Members.mainimage'
        db.alter_column('members', 'mainimage', self.gf('django.db.models.fields.files.ImageField')(max_length=150L))

        # Changing field 'Members.emailopen_date'
        db.alter_column('members', 'emailopen_date', self.gf('django.db.models.fields.DateField')(default=0))
        # Adding field 'VendorsAddcontact.reciprocal'
        db.add_column('vendors_addcontact', 'reciprocal',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10L, blank=True),
                      keep_default=False)


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
            'emailopen_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gfirst_name': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'glast_name': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'hero_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
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
            'members': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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