# Generated by Django 3.1 on 2020-09-06 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0006_auto_20200906_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliverytime',
            old_name='Address',
            new_name='address',
        ),
    ]
