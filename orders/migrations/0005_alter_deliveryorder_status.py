# Generated by Django 4.2.17 on 2025-03-31 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_deliveryorder_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryorder',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.statusmodel'),
        ),
    ]
