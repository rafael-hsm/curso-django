# Generated by Django 3.2.8 on 2021-10-14 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('titulo', models.CharField(max_length=64)),
                ('publico', models.TextField()),
                ('descricao', models.TextField()),
                ('slug', models.SlugField(null=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('titulo', models.CharField(max_length=64)),
                ('slug', models.SlugField(null=True)),
                ('vimeo_id', models.CharField(default='1', max_length=32)),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modulos.modulo')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
