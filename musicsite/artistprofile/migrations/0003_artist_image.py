# Generated by Django 5.0.3 on 2024-04-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistprofile', '0002_artist_is_active_artist_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
