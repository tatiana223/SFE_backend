# Generated by Django 4.2.7 on 2024-12-01 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_responses_vacancies'),
    ]

    operations = [
        migrations.AddField(
            model_name='responses',
            name='interview_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
