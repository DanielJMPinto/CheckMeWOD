# Generated by Django 3.0.4 on 2020-04-30 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkmewod', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videosubmission',
            name='video_file',
            field=models.FileField(null=True, upload_to='checkmewod/uploaded_files/', verbose_name=''),
        ),
    ]
