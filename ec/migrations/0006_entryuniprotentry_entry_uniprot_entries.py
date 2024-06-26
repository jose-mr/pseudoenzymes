# Generated by Django 5.0.4 on 2024-04-10 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0005_entry_comments_entry_description_and_more'),
        ('uniprot', '0004_remove_entry_keywords_entry_keywords'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryUniProtEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ec.entry')),
                ('uniprot_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uniprot.entry')),
            ],
            options={
                'unique_together': {('entry', 'uniprot_entry')},
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='uniprot_entries',
            field=models.ManyToManyField(related_name='ec_entries', through='ec.EntryUniProtEntry', to='uniprot.entry'),
        ),
    ]
