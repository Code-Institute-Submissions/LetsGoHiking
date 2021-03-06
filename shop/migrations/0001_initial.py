# Generated by Django 3.1.2 on 2020-10-19 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_description', models.TextField()),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(choices=[('Patches', 'Patches'), ('Stickers', 'Stickers'), ('Hats', 'Hats'), ('WaterBottle', 'WaterBottle')], max_length=20, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.category')),
            ],
        ),
    ]
