# Generated by Django 5.0.4 on 2024-04-09 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0004_alter_term_aspect_termuniprotentry'),
        ('uniprot', '0004_remove_entry_keywords_entry_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='uniprot_entries',
            field=models.ManyToManyField(related_name='go_terms', through='go.TermUniProtEntry', to='uniprot.entry'),
        ),
    ]
