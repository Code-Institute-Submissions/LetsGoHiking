# Generated by Django 3.1.2 on 2020-10-26 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_county',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_phone_number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_postcode',
            new_name='postcode',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_street_address1',
            new_name='street_address1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_street_address2',
            new_name='street_address2',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_town_or_city',
            new_name='town_or_city',
        ),
    ]
