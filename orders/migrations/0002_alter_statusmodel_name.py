# Generated by Django 5.1.4 on 2024-12-08 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusmodel',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
