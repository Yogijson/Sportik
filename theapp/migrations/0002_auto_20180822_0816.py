# Generated by Django 2.1 on 2018-08-22 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='equipment_pic',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='sport',
            name='sport_logo',
            field=models.FileField(upload_to=''),
        ),
    ]