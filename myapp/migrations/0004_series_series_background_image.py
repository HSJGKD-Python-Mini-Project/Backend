# Generated by Django 3.2.9 on 2021-12-23 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20211204_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='series_background_image',
            field=models.ImageField(blank=True, null=True, upload_to='series/bgi'),
        ),
    ]
