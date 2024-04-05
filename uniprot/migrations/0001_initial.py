# Generated by Django 5.0.4 on 2024-04-05 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('ac', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='primary accession number')),
                ('secondary_ac', models.JSONField(default=list, verbose_name='secondary accession numbers')),
                ('name', models.TextField()),
                ('comment', models.TextField()),
                ('taxid', models.IntegerField(verbose_name='NCBI TaxId')),
                ('keywords', models.JSONField(default=list)),
                ('seq', models.TextField()),
            ],
        ),
    ]
