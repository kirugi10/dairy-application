# Generated by Django 2.1.7 on 2019-03-03 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalcategory',
            name='related_vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AnimalCategory', to='dairyapp.vendorledger'),
        ),
    ]