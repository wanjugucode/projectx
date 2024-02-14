# Generated by Django 5.0.1 on 2024-01-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True, null=True)),
                ('expiry_date', models.DateTimeField(null=True)),
                ('title', models.CharField(max_length=25, null=True)),
                ('subject', models.CharField(max_length=25, null=True)),
                ('course_image', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]