# Generated by Django 4.2.3 on 2023-08-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_online_shop', '0003_onlineshop_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlineshop',
            name='image',
            field=models.ImageField(default='', upload_to='online_shop/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
