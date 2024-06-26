# Generated by Django 5.0.4 on 2024-04-09 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco', '0003_relation'),
        ('go', '0003_alter_term_aspect_relation'),
        ('uniprot', '0004_remove_entry_keywords_entry_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='aspect',
            field=models.TextField(choices=[('molecular_function', 'molecular_function'), ('cellular_component', 'cellular_component'), ('biological_process', 'biological_process')]),
        ),
        migrations.CreateModel(
            name='TermUniProtEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualifier', models.CharField(db_index=True, max_length=127)),
                ('eco_term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eco.term')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='go.term')),
                ('uniprot_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uniprot.entry')),
            ],
            options={
                'unique_together': {('term', 'uniprot_entry', 'qualifier', 'eco_term')},
            },
        ),
    ]
