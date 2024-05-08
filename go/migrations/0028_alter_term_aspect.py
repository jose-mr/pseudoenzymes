# Generated by Django 5.0.4 on 2024-05-08 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0027_alter_term_aspect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='aspect',
            field=models.TextField(choices=[('molecular_function', 'molecular_function'), ('cellular_component', 'cellular_component'), ('biological_process', 'biological_process')]),
        ),
    ]
