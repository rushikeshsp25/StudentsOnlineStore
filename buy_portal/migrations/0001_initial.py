# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-04 12:31
from __future__ import unicode_literals

import buy_portal.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[(b'Other', b'Other'), (b'Book', b'Book'), (b'Instrument', b'Instrument'), (b'Project', b'Project')], default=b'Other', max_length=10)),
                ('item_name', models.CharField(max_length=100)),
                ('mrp_price', models.IntegerField()),
                ('selling_price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=buy_portal.models.get_image_path)),
                ('description', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
