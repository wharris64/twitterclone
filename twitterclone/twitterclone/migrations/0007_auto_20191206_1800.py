# Generated by Django 2.2.6 on 2019-12-06 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0006_auto_20191206_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='twitteruser',
            old_name='name',
            new_name='username',
        ),
    ]
