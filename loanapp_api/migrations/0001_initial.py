# Generated by Django 5.0.13 on 2025-03-18 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loandata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pool', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('hosue_number', models.IntegerField()),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip_code', models.IntegerField()),
                ('note_date', models.DateField()),
                ('interest', models.FloatField()),
                ('payment', models.FloatField()),
                ('original_balance', models.FloatField()),
                ('current_balance', models.FloatField()),
                ('appraisal', models.FloatField()),
            ],
        ),
    ]
