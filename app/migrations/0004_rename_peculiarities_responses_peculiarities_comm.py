# Generated by Django 4.2.7 on 2024-10-22 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_responses_education_responses_experience_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='responses',
            old_name='peculiarities',
            new_name='peculiarities_comm',
        ),
    ]