# Generated by Django 2.0 on 2019-11-19 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0004_product_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
