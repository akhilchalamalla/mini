# Generated by Django 3.0.8 on 2020-10-01 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='name',
        ),
    ]
