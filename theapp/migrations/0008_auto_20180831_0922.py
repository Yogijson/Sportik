# Generated by Django 2.1 on 2018-08-31 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0007_auto_20180831_0711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='emailid',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
    ]
