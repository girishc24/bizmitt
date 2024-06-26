# Generated by Django 5.0.3 on 2024-04-17 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_employee_cno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier', models.CharField(max_length=200, unique=True)),
                ('cno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companytier', to='company.company')),
            ],
        ),
    ]
