# Generated by Django 3.1 on 2020-08-26 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0002_auto_20200826_0459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addresstype', models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120)),
                ('address_line1', models.CharField(max_length=120)),
                ('address_line2', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=120)),
                ('postal_code', models.CharField(max_length=120)),
                ('billing_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.billingprofile')),
            ],
        ),
    ]
