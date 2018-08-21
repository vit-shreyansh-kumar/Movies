# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=40)),
                ('lname', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('storyline', models.TextField(max_length=300, null=True, blank=True)),
                ('budget', models.CharField(max_length=50, null=True, blank=True)),
                ('score', models.FloatField(max_length=3)),
                ('actor', models.ManyToManyField(related_name='actor_name', to='movies.Actor')),
                ('certificate', models.ForeignKey(to='movies.Certificate')),
                ('country', models.ForeignKey(to='movies.Country')),
                ('director', models.ManyToManyField(related_name='director_name', to='movies.Actor')),
                ('genres', models.ManyToManyField(to='movies.Genres')),
                ('language', models.ForeignKey(to='movies.Language')),
            ],
        ),
    ]
