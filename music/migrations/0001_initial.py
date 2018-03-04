# Generated by Django 2.0.2 on 2018-02-28 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_Name', models.CharField(max_length=100)),
                ('album_tittle', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=20)),
                ('album_logo', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=100)),
                ('file_type', models.CharField(max_length=50)),
                ('artist', models.CharField(max_length=100)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
            ],
        ),
    ]
