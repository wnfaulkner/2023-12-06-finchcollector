# Generated by Django 5.0 on 2023-12-08 23:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='flight date')),
                ('cargo', models.CharField(choices=[('B', 'Beer'), ('C', 'Coconut'), ('D', 'Denisovan remains')], default='B', max_length=1)),
                ('finch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.finch')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]