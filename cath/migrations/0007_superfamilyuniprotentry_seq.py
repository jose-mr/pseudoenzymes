# Generated by Django 5.0.4 on 2024-05-07 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cath', '0006_alter_superfamily_name_alter_superfamily_number'),
        ('uniprot', '0007_alter_entry_seq'),
    ]

    operations = [
        migrations.AddField(
            model_name='superfamilyuniprotentry',
            name='seq',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='uniprot.sequence'),
        ),
    ]