# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 12:40
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ayah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='Number')),
                ('text', models.TextField()),
            ],
            options={
                'ordering': ['sura', 'number'],
            },
        ),
        migrations.CreateModel(
            name='Sura',
            fields=[
                ('index', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Sura')),
            ],
            options={
                'ordering': ['index'],
            },
        ),
        migrations.AddField(
            model_name='ayah',
            name='sura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ayat', to='quran_text.Sura'),
        ),
        migrations.AlterUniqueTogether(
            name='ayah',
            unique_together=set([('number', 'sura')]),
        ),
    ]
