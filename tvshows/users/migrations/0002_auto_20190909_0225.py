# Generated by Django 2.1.2 on 2019-09-09 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='saved_shows',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='saved_shows',
            field=models.ManyToManyField(blank=True, to='users.TvShow'),
        ),
    ]
