# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Employee.photo'
        db.delete_column(u'personnel_employee', 'photo')

        # Adding field 'Employee.image'
        db.add_column(u'personnel_employee', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Specialisation.icon'
        db.delete_column(u'personnel_specialisation', 'icon')

        # Adding field 'Specialisation.image'
        db.add_column(u'personnel_specialisation', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Employee.photo'
        db.add_column(u'personnel_employee', 'photo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Employee.image'
        db.delete_column(u'personnel_employee', 'image')

        # Adding field 'Specialisation.icon'
        db.add_column(u'personnel_specialisation', 'icon',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Specialisation.image'
        db.delete_column(u'personnel_specialisation', 'image')


    models = {
        u'personnel.employee': {
            'Meta': {'object_name': 'Employee'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'specialisation': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['personnel.Specialisation']", 'symmetrical': 'False'})
        },
        u'personnel.specialisation': {
            'Meta': {'object_name': 'Specialisation'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['personnel']