# Generated by Django 5.0.3 on 2024-03-30 04:08

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0019_delete_scholarship'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarships',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
