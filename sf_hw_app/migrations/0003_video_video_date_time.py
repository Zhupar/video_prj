# Generated by Django 3.2.13 on 2022-04-21 18:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sf_hw_app', '0002_auto_20220420_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_date_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='video_date_time'),
            preserve_default=False,
        ),
    ]
