# Generated by Django 3.2.8 on 2021-10-09 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=32)),
                ('slug', models.SlugField(max_length=32)),
                ('vimeo_id', models.CharField(max_length=32)),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
