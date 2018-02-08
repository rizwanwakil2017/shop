# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=150)),
                ('publisher', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, related_name='children', to='shop.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='catalog',
            field=models.ForeignKey(default=1, related_name='categories', to='shop.Catalog'),
            preserve_default=False,
        ),
    ]
