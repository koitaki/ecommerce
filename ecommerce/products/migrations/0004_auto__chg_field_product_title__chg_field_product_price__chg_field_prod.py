# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Product.title'
        db.alter_column(u'products_product', 'title', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Product.price'
        db.alter_column(u'products_product', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2))

        # Changing field 'Product.sale_price'
        db.alter_column(u'products_product', 'sale_price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))
        # Adding unique constraint on 'Product', fields ['slug']
        db.create_unique(u'products_product', ['slug'])

        # Adding unique constraint on 'Product', fields ['title', 'slug']
        db.create_unique(u'products_product', ['title', 'slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Product', fields ['title', 'slug']
        db.delete_unique(u'products_product', ['title', 'slug'])

        # Removing unique constraint on 'Product', fields ['slug']
        db.delete_unique(u'products_product', ['slug'])


        # Changing field 'Product.title'
        db.alter_column(u'products_product', 'title', self.gf('django.db.models.fields.CharField')(max_length=120))

        # Changing field 'Product.price'
        db.alter_column(u'products_product', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=100, decimal_places=2))

        # Changing field 'Product.sale_price'
        db.alter_column(u'products_product', 'sale_price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=100, decimal_places=2))

    models = {
        u'products.product': {
            'Meta': {'unique_together': "(('title', 'slug'),)", 'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '29.99', 'max_digits': '10', 'decimal_places': '2'}),
            'sale_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'products.productimage': {
            'Meta': {'object_name': 'ProductImage'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"}),
            'thumbnail': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['products']