# Generated by Django 2.2.6 on 2019-12-06 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0005_auto_20191206_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='retweets',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
