# Generated by Django 3.0.8 on 2020-09-20 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200919_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eregister',
            name='grade',
            field=models.TextField(),
        ),
    ]
