# Generated by Django 3.1 on 2020-09-12 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0008_remove_address_postal_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliverytime',
            name='time',
        ),
        migrations.AlterField(
            model_name='deliverytime',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
