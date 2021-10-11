# Generated by Django 3.2.8 on 2021-10-14 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0003_alter_aula_vimeo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='aula',
            name='vimeo_id',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='modulo',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
