# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Articles.publish_datetime'
        db.alter_column(u'aggregator_articles', 'publish_datetime', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):

        # Changing field 'Articles.publish_datetime'
        db.alter_column(u'aggregator_articles', 'publish_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True))

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
            'mainthumb': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'original_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'publish_datetime': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'source_link': ('django.db.models.fields.CharField', [], {'max_length': '700'}),
            'source_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'source_site': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
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