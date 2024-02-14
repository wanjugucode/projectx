# Generated by Django 5.0.2 on 2024-02-13 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0012_scholarshipapplication_approved_scholarship'),
        ('userprofile', '0003_alter_userprofile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='applications',
            field=models.ManyToManyField(related_name='user_profiles', to='scholarships.scholarshipapplication'),
        ),
    ]