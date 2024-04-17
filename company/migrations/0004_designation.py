# Generated by Django 5.0.3 on 2024-04-17 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_company_business_alter_company_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=200, unique=True)),
                ('cno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companyname', to='company.company')),
            ],
        ),
    ]