# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DescriptionTask'
        db.create_table('tasks_descriptiontask', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('completion_code', self.gf('django.db.models.fields.CharField')(default='c6648308daac43f9859de17590147b87', unique=True, max_length=32)),
            ('approved', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal('tasks', ['DescriptionTask'])

        # Adding model 'DescriptionQuestion'
        db.create_table('tasks_descriptionquestion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(related_name='questions', to=orm['tasks.DescriptionTask'])),
            ('scene', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenes.Scene'])),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='descriptions', to=orm['scenes.Entity'])),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('tasks', ['DescriptionQuestion'])


    def backwards(self, orm):
        # Deleting model 'DescriptionTask'
        db.delete_table('tasks_descriptiontask')

        # Deleting model 'DescriptionQuestion'
        db.delete_table('tasks_descriptionquestion')


    models = {
        'scenes.entity': {
            'Meta': {'object_name': 'Entity'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'scene': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entities'", 'to': "orm['scenes.Scene']"})
        },
        'scenes.scene': {
            'Meta': {'object_name': 'Scene'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'tasks.descriptionquestion': {
            'Meta': {'object_name': 'DescriptionQuestion'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'descriptions'", 'to': "orm['scenes.Entity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'scene': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenes.Scene']"}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': "orm['tasks.DescriptionTask']"})
        },
        'tasks.descriptiontask': {
            'Meta': {'object_name': 'DescriptionTask'},
            'approved': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'completion_code': ('django.db.models.fields.CharField', [], {'default': "'fa0b5728afb348d3b69ba1fba95afdf5'", 'unique': 'True', 'max_length': '32'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tasks']