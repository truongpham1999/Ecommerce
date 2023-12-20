# Generated by Django 4.2.7 on 2023-12-18 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('address1', models.CharField(max_length=400)),
                ('address2', models.CharField(max_length=400)),
                ('city', models.CharField(max_length=250)),
                ('district', models.CharField(max_length=250)),
                ('ward', models.CharField(max_length=250)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_address', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Shipping Addresses',
            },
        ),
    ]