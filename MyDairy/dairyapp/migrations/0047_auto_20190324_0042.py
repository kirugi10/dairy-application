# Generated by Django 2.1.7 on 2019-03-23 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0046_profile_joining_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='joining_data',
            field=models.DateField(),
        ),
    ]