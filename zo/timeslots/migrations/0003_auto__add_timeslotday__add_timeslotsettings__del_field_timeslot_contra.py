# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TimeSlotDay'
        db.create_table('timeslots_timeslotday', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contragent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contragents.Contragent'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('duration', self.gf('django.db.models.fields.IntegerField')(default=30)),
            ('capacity', self.gf('django.db.models.fields.IntegerField')()),
            ('aviability', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('timeslots', ['TimeSlotDay'])

        # Adding model 'TimeSlotSettings'
        db.create_table('timeslots_timeslotsettings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('duration', self.gf('django.db.models.fields.IntegerField')()),
            ('capacity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('timeslots', ['TimeSlotSettings'])

        # Deleting field 'Timeslot.contragent'
        db.delete_column('timeslots_timeslot', 'contragent_id')

        # Deleting field 'Timeslot.duration'
        db.delete_column('timeslots_timeslot', 'duration')

        # Deleting field 'Timeslot.date'
        db.delete_column('timeslots_timeslot', 'date')

        # Adding field 'Timeslot.day'
        db.add_column('timeslots_timeslot', 'day',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=300, to=orm['timeslots.TimeSlotDay']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'TimeSlotDay'
        db.delete_table('timeslots_timeslotday')

        # Deleting model 'TimeSlotSettings'
        db.delete_table('timeslots_timeslotsettings')

        # Adding field 'Timeslot.contragent'
        db.add_column('timeslots_timeslot', 'contragent',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['contragents.Contragent']),
                      keep_default=False)

        # Adding field 'Timeslot.duration'
        db.add_column('timeslots_timeslot', 'duration',
                      self.gf('django.db.models.fields.IntegerField')(default=30),
                      keep_default=False)

        # Adding field 'Timeslot.date'
        db.add_column('timeslots_timeslot', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 2, 21, 0, 0)),
                      keep_default=False)

        # Deleting field 'Timeslot.day'
        db.delete_column('timeslots_timeslot', 'day_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        'profile.userprofile': {
            'Meta': {'ordering': "['user']", 'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'user_contr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contragents.Contragent']", 'null': 'True', 'blank': 'True'})
        },
        'timeslots.appointment': {
            'Meta': {'object_name': 'Appointment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timeslot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timeslots.Timeslot']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profile.UserProfile']"})
        },
        'timeslots.timeslot': {
            'Meta': {'object_name': 'Timeslot'},
            'capacity': ('django.db.models.fields.IntegerField', [], {}),
            'day': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timeslots.TimeSlotDay']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        'timeslots.timeslotday': {
            'Meta': {'object_name': 'TimeSlotDay'},
            'aviability': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'capacity': ('django.db.models.fields.IntegerField', [], {}),
            'contragent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contragents.Contragent']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'duration': ('django.db.models.fields.IntegerField', [], {'default': '30'}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        'timeslots.timeslotsettings': {
            'Meta': {'object_name': 'TimeSlotSettings'},
            'capacity': ('django.db.models.fields.IntegerField', [], {}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['timeslots']