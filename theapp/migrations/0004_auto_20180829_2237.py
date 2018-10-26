# Generated by Django 2.1 on 2018-08-29 17:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0003_auto_20180823_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 8, 29, 17, 6, 6, 576660, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='stock',
            field=models.PositiveIntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10),
        ),
    ]