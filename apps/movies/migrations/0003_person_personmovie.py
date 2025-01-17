# Generated by Django 3.2.8 on 2021-11-12 17:08

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('movies', '0002_auto_20211112_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdb_id', models.CharField(blank=True, max_length=10, null=True, verbose_name='nconst')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='primaryName')),
                ('birth_year', models.DateField(blank=True, null=True, verbose_name='birthYear')),
                ('death_year', models.DateField(blank=True, null=True, verbose_name='deathYear')),
            ],
        ),
        migrations.CreateModel(
            name='PersonMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='ordering')),
                ('category', models.CharField(blank=True, choices=[('AC-R', 'actor'), ('AC-S', 'actress'),
                                                                   ('CIN', 'cinematographer'), ('COM', 'composer'),
                                                                   ('DIR', 'director'), ('ED', 'editor'),
                                                                   ('PR', 'producer'), ('SEL', 'self'),
                                                                   ('WR', 'writer')], max_length=100, null=True,
                                              verbose_name='category')),
                ('job', models.CharField(blank=True, choices=[('CO-D', 'co-director'), ('COM', 'comic strip'),
                                                              ('DIR-P', 'director of photography'), ('NOV', 'novel'),
                                                              ('PL', 'play'), ('PO', 'poem'), ('PR', 'producer'),
                                                              ('SC', 'scenario'), ('SC-P', 'screen play'),
                                                              ('ST', 'story'), ('WR', 'writer')], max_length=100,
                                         null=True, verbose_name='job')),
                ('characters', django.contrib.postgres.fields.ArrayField(
                    base_field=models.CharField(max_length=255, verbose_name='characters'), blank=True, null=True,
                    size=None)),
                ('movie_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                               to='movies.movie')),
                ('person_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                                to='movies.person')),
            ],
        ),
    ]
