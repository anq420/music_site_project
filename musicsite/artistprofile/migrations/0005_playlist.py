# Generated by Django 5.0.3 on 2024-04-02 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistprofile', '0004_remove_album_songs_album_songs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('songs', models.ManyToManyField(to='artistprofile.song')),
            ],
        ),
    ]
