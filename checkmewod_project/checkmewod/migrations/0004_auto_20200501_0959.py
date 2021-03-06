# Generated by Django 3.0.4 on 2020-05-01 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkmewod', '0003_auto_20200430_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('start_date', models.TextField(null=True)),
                ('end_date', models.TextField(null=True)),
                ('start_time', models.TextField(null=True)),
                ('end_time', models.TextField(null=True)),
                ('registration_url', models.TextField(null=True)),
                ('website_url', models.TextField(null=True)),
                ('country', models.TextField(null=True)),
                ('location', models.TextField(null=True)),
                ('street', models.TextField(null=True)),
                ('zipcode', models.TextField(null=True)),
                ('price', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('logo', models.ImageField(null=True, upload_to='checkmewod/uploaded_files')),
            ],
        ),
        migrations.AddField(
            model_name='videosubmission',
            name='video_status',
            field=models.TextField(null=True),
        ),
    ]
