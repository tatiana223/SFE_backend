# Generated by Django 4.2.7 on 2024-10-22 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_id_vacancies_vacancies_id_vacancy_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsesvacancies',
            name='is_main',
        ),
    ]