# Generated by Django 5.0.3 on 2024-04-02 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistprofile', '0003_artist_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='songs',
        ),
        migrations.AddField(
            model_name='album',
            name='songs',
            field=models.ManyToManyField(default='', to='artistprofile.song'),
        ),
    ]
