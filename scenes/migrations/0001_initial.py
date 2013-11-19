# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Scene'
        db.create_table('scenes_scene', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('scenes', ['Scene'])

        # Adding model 'Entity'
        db.create_table('scenes_entity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('scene', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entities', to=orm['scenes.Scene'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('scenes', ['Entity'])

        # Adding model 'GeneratedDescription'
        db.create_table('scenes_generateddescription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='generated_descriptions', to=orm['scenes.GeneratedDescription'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('corpus_size', self.gf('django.db.models.fields.IntegerField')()),
            ('representation_model', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal('scenes', ['GeneratedDescription'])

    def backwards(self, orm):
        # Deleting model 'Scene'
        db.delete_table('scenes_scene')

        # Deleting model 'Entity'
        db.delete_table('scenes_entity')

        # Deleting model 'GeneratedDescription'
        db.delete_table('scenes_generateddescriptions')


    models = {
        'scenes.generateddescription': {
            'Meta': {'object_name': 'GeneratedDescription'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'generated_descriptions'", 'to': "orm['scenes.GeneratedDescription']"}),
            'corpus_size': ('django.db.models.fields.IntegerField', [], {}),
            'representation_model': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
        },
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
        }
    }

    complete_apps = ['scenes']