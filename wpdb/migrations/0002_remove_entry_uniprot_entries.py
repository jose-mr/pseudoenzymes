# Generated by Django 5.0.4 on 2024-05-22 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wpdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='uniprot_entries',
        ),
    ]
