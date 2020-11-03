# Generated by Django 3.1.2 on 2020-11-03 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20201029_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='country',
            new_name='default_country',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='county',
            new_name='default_county',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='postcode',
            new_name='default_phone_number',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='street_address1',
            new_name='default_street_address1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='street_address2',
            new_name='default_street_address2',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='town_or_city',
            new_name='default_town_or_city',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]