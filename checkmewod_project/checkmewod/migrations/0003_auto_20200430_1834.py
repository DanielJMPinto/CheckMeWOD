# Generated by Django 3.0.4 on 2020-04-30 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkmewod', '0002_videosubmission_video_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='videosubmission',
            name='exercise_in_video',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='videosubmission',
            name='number_correct_reps',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='videosubmission',
            name='number_incorrect_reps',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='videosubmission',
            name='number_reps',
            field=models.TextField(null=True),
        ),
    ]