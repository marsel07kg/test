# Generated by Django 5.0.6 on 2024-06-26 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0002_alter_shop_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
