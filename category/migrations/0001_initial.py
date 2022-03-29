# Generated by Django 3.1 on 2022-03-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cat_name', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('cat_image', models.ImageField(upload_to='photos/category')),
            ],
            options={
                'verbose_name': 'categorys',
                'verbose_name_plural': 'categories',
            },
        ),
    ]