# Generated by Django 2.1.2 on 2019-09-14 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190912_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='vote_average',
            field=models.FloatField(),
        ),
    ]
