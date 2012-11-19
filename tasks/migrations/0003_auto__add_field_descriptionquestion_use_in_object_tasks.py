# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DescriptionQuestion.use_in_object_tasks'
        db.add_column('tasks_descriptionquestion', 'use_in_object_tasks',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DescriptionQuestion.use_in_object_tasks'
        db.delete_column('tasks_descriptionquestion', 'use_in_object_tasks')


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
            'location_description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'object_description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'scene': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenes.Scene']"}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': "orm['tasks.DescriptionTask']"}),
            'use_in_object_tasks': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'tasks.descriptiontask': {
            'Meta': {'object_name': 'DescriptionTask'},
            'approved': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'completion_code': ('django.db.models.fields.CharField', [], {'default': "'a1780ecc6cf04a7c90a049d8f6917be4'", 'unique': 'True', 'max_length': '32'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tasks']