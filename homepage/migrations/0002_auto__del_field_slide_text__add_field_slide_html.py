# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Slide.text'
        db.delete_column(u'homepage_slide', 'text')

        # Adding field 'Slide.html'
        db.add_column(u'homepage_slide', 'html',
                      self.gf('tinymce.models.HTMLField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Slide.text'
        db.add_column(u'homepage_slide', 'text',
                      self.gf('tinymce.models.HTMLField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Slide.html'
        db.delete_column(u'homepage_slide', 'html')


    models = {
        u'homepage.slide': {
            'Meta': {'object_name': 'Slide'},
            'html': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        },
        u'homepage.tab': {
            'Meta': {'object_name': 'Tab'},
            'html': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['homepage']