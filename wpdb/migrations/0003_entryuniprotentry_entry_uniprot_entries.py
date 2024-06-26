# Generated by Django 5.0.4 on 2024-05-22 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniprot', '0008_multisequencealignment'),
        ('wpdb', '0002_remove_entry_uniprot_entries'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryUniProtEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdb_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uniprot_entries_through', to='wpdb.entry')),
                ('uniprot_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pdb_entries_through', to='uniprot.entry')),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='uniprot_entries',
            field=models.ManyToManyField(related_name='pdb_entries', through='wpdb.EntryUniProtEntry', to='uniprot.entry'),
        ),
    ]
