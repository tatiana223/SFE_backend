# Generated by Django 4.2.7 on 2024-12-02 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_responses_interview_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancies',
            old_name='id_vacancy',
            new_name='vacancy_id',
        ),
    ]