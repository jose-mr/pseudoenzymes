# Generated by Django 5.0.4 on 2024-05-22 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniprot', '0008_multisequencealignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='reviewed',
            field=models.BooleanField(default=True),
        ),
    ]
