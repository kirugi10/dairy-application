# Generated by Django 2.1.7 on 2019-03-20 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0032_auto_20190320_1626'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]