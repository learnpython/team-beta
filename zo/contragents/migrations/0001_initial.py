# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('contragents_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='\xd1\x80\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd1\x81\xd0\xba\xd0\xb0\xd1\x8f \xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', null=True, to=orm['contragents.Category'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('contragents', ['Category'])

        # Adding model 'Contragent'
        db.create_table('contragents_contragent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('main_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contragents.Category'])),
            ('contr_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('detail', self.gf('django.db.models.fields.TextField')()),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contragents.CityRegion'])),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contragents.City'])),
            ('street1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('street2', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('building', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(max_length=10, null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(max_length=10, null=True, blank=True)),
            ('visits', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('contragents', ['Contragent'])

        # Adding M2M table for field additional_categories on 'Contragent'
        db.create_table('contragents_contragent_additional_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contragent', models.ForeignKey(orm['contragents.contragent'], null=False)),
            ('category', models.ForeignKey(orm['contragents.category'], null=False))
        ))
        db.create_unique('contragents_contragent_additional_categories', ['contragent_id', 'category_id'])

        # Adding model 'City'
        db.create_table('contragents_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('contragents', ['City'])

        # Adding model 'CityRegion'
        db.create_table('contragents_cityregion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('contragents', ['CityRegion'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('contragents_category')

        # Deleting model 'Contragent'
        db.delete_table('contragents_contragent')

        # Removing M2M table for field additional_categories on 'Contragent'
        db.delete_table('contragents_contragent_additional_categories')

        # Deleting model 'City'
        db.delete_table('contragents_city')

        # Deleting model 'CityRegion'
        db.delete_table('contragents_cityregion')


    models = {
        'contragents.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'\\xd1\\x80\\xd0\\xbe\\xd0\\xb4\\xd0\\xb8\\xd1\\x82\\xd0\\xb5\\xd0\\xbb\\xd1\\x8c\\xd1\\x81\\xd0\\xba\\xd0\\xb0\\xd1\\x8f \\xd0\\xba\\xd0\\xb0\\xd1\\x82\\xd0\\xb5\\xd0\\xb3\\xd0\\xbe\\xd1\\x80\\xd0\\xb8\\xd1\\x8f'", 'null': 'True', 'to': "orm['contragents.Category']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'contragents.city': {
            'Meta': {'object_name': 'City'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contragents.cityregion': {
            'Meta': {'object_name': 'CityRegion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'contragents.contragent': {
            'Meta': {'ordering': "['name']", 'object_name': 'Contragent'},
            'additional_categories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'additional_contragents'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['contragents.Category']"}),
            'building': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contragents.City']"}),
            'contr_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'detail': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'main_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contragents.Category']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contragents.CityRegion']"}),
            'street1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'street2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'visits': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        }
    }

    complete_apps = ['contragents']