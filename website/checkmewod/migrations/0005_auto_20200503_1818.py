# Generated by Django 3.0.5 on 2020-05-03 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkmewod', '0004_auto_20200503_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_Logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/event_logos/'),
        ),
    ]