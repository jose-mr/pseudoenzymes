# Generated by Django 5.0.4 on 2024-04-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cath', '0004_remove_superfamilyuniprotentry_evalue'),
        ('uniprot', '0004_remove_entry_keywords_entry_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='superfamily',
            name='uniprot_entries',
            field=models.ManyToManyField(related_name='cath_superfamilies', through='cath.SuperfamilyUniprotEntry', to='uniprot.entry'),
        ),
    ]
