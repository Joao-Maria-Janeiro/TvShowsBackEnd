# Generated by Django 2.1.2 on 2019-09-12 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190909_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='suggested_shows',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='userprofile_requests', to='users.TvShow'),
            preserve_default=False,
        ),
    ]
