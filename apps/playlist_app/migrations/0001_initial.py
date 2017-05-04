# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music_app', '0001_initial'),
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listener',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=512)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='listener',
            name='playlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listeners', to='playlist_app.Playlist'),
        ),
        migrations.AddField(
            model_name='listener',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_playlists', to='user_app.User'),
        ),
        migrations.AddField(
            model_name='addition',
            name='playlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlist_app.Playlist'),
        ),
        migrations.AddField(
            model_name='addition',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.Song'),
        ),
    ]
