# Generated by Django 4.0.3 on 2022-03-30 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vid_con', '0007_alter_video_play_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='play_url',
            field=models.FileField(null=True, upload_to='videofiles', verbose_name=''),
        ),
    ]