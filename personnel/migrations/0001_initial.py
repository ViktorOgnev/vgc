# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Specialisation'
        db.create_table(u'personnel_specialisation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'personnel', ['Specialisation'])

        # Adding model 'Employee'
        db.create_table(u'personnel_employee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'personnel', ['Employee'])

        # Adding M2M table for field specialisation on 'Employee'
        m2m_table_name = db.shorten_name(u'personnel_employee_specialisation')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('employee', models.ForeignKey(orm[u'personnel.employee'], null=False)),
            ('specialisation', models.ForeignKey(orm[u'personnel.specialisation'], null=False))
        ))
        db.create_unique(m2m_table_name, ['employee_id', 'specialisation_id'])


    def backwards(self, orm):
        # Deleting model 'Specialisation'
        db.delete_table(u'personnel_specialisation')

        # Deleting model 'Employee'
        db.delete_table(u'personnel_employee')

        # Removing M2M table for field specialisation on 'Employee'
        db.delete_table(db.shorten_name(u'personnel_employee_specialisation'))


    models = {
        u'personnel.employee': {
            'Meta': {'object_name': 'Employee'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'specialisation': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['personnel.Specialisation']", 'symmetrical': 'False'})
        },
        u'personnel.specialisation': {
            'Meta': {'object_name': 'Specialisation'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['personnel']