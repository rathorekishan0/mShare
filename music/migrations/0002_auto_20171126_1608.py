# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 10:38
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=200)),
                ('date_comment', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_comment'],
            },
        ),
        migrations.CreateModel(
            name='music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songname', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=30)),
                ('songphoto', models.FileField(upload_to='static/music/songimages', validators=[django.core.validators.FileExtensionValidator(['jpeg', 'png', 'bmp', 'jpg'], 'file exteion not valid')])),
                ('songupload', models.FileField(upload_to='static/music/songs', validators=[django.core.validators.FileExtensionValidator(['mp3', 'aac'], 'file extension not valid')])),
                ('likenum', models.IntegerField(default=0)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('public', models.BooleanField(default=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('favourites', models.ManyToManyField(blank=True, related_name='favourite_by', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='liked_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(blank=True, max_length=250, null=True)),
                ('name', models.CharField(max_length=100)),
                ('userphoto', models.ImageField(null=True, upload_to='static/music/userimages', validators=[django.core.validators.FileExtensionValidator(['jpeg', 'png', 'bmp', 'jpg'], 'file exteion not valid')])),
                ('description', models.CharField(max_length=200)),
                ('first', models.BooleanField(default=True)),
                ('prefferedgenre', models.CharField(max_length=20)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('activated', models.BooleanField(default=False)),
                ('followers', models.ManyToManyField(blank=True, related_name='is_following', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.DeleteModel(
            name='album',
        ),
        migrations.DeleteModel(
            name='song',
        ),
        migrations.AddField(
            model_name='comments',
            name='song_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.music'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
