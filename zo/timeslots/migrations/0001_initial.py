# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Timeslot'
        db.create_table('timeslots_timeslot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contragent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contragents.Contragent'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('time', self.gf('django.db.models.fields.TimeField')()),
            ('duration', self.gf('django.db.models.fields.IntegerField')()),
            ('capacity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('timeslots', ['Timeslot'])


    def backwards(self, orm):
        # Deleting model 'Timeslot'
        db.delete_table('timeslots_timeslot')


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
            'detail': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'main_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contragents.Category']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contragents.CityRegion']"}),
            'street1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'street2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'visits': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        },
        'timeslots.timeslot': {
            'Meta': {'object_name': 'Timeslot'},
            'capacity': ('django.db.models.fields.IntegerField', [], {}),
            'contragent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contragents.Contragent']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['timeslots']