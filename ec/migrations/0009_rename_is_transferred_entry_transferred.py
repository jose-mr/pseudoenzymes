# Generated by Django 5.0.4 on 2024-04-10 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0008_remove_entry_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='is_transferred',
            new_name='transferred',
        ),
    ]
