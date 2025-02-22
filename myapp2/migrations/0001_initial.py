# Generated by Django 5.0.1 on 2024-01-25 11:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_password', message='Password must contain at least one letter and one number.', regex='^(?=.*[0-9])(?=.*[a-zA-Z])')])),
            ],
        ),
        migrations.CreateModel(
            name='UserSignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_password', message='Password must contain at least one letter and one number.', regex='^(?=.*[0-9])(?=.*[a-zA-Z])')])),
            ],
        ),
    ]
