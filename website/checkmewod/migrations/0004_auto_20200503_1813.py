# Generated by Django 3.0.5 on 2020-05-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkmewod', '0003_auto_20200502_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_Logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/event_logos/'),
        ),
    ]