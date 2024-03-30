# Generated by Django 5.0.3 on 2024-03-13 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0017_rename_report_reportinaccuracy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.CharField(max_length=255)),
                ('deadline', models.CharField(max_length=255)),
                ('eligibility_criteria', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='scholarship_images/')),
            ],
        ),
    ]