# Generated by Django 3.1.2 on 2020-10-18 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='challenge_descent',
        ),
        migrations.AddField(
            model_name='challenge',
            name='challenge_award_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
