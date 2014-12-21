# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Articles'
        db.create_table(u'aggregator_articles', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('article_text', self.gf('django.db.models.fields.TextField')()),
            ('source_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('source_site', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('source_link', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('original_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('publish_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'aggregator', ['Articles'])

        # Adding model 'ArticleImages'
        db.create_table(u'aggregator_articleimages', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('articles', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aggregator.Articles'])),
            ('image_link', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('image_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'aggregator', ['ArticleImages'])

        # Adding model 'Tags'
        db.create_table(u'aggregator_tags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('articles', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aggregator.Articles'])),
            ('tagname', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'aggregator', ['Tags'])


    def backwards(self, orm):
        # Deleting model 'Articles'
        db.delete_table(u'aggregator_articles')

        # Deleting model 'ArticleImages'
        db.delete_table(u'aggregator_articleimages')

        # Deleting model 'Tags'
        db.delete_table(u'aggregator_tags')


    models = {
        u'aggregator.articleimages': {
            'Meta': {'object_name': 'ArticleImages'},
            'articles': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['aggregator.Articles']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_link': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'image_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'aggregator.articles': {
            'Meta': {'object_name': 'Articles'},
            'article_text': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'original_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'publish_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'source_link': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'source_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'source_site': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'aggregator.tags': {
            'Meta': {'object_name': 'Tags'},
            'articles': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['aggregator.Articles']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tagname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['aggregator']