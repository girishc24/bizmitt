# Generated by Django 5.0.3 on 2024-04-02 04:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='business',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='phoneno',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=200, unique=True)),
                ('cno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='company.company')),
            ],
        ),
    ]
