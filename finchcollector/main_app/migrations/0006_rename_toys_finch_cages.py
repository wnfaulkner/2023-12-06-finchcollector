# Generated by Django 5.0 on 2023-12-10 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_cage_cage_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finch',
            old_name='toys',
            new_name='cages',
        ),
    ]
