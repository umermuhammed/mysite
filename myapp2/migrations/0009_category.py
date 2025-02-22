# Generated by Django 5.0.1 on 2024-04-04 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0008_order_feedback_category_alter_order_company_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_name', models.CharField(max_length=100)),
                ('selection_type', models.CharField(max_length=100)),
                ('cr_number', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=100)),
                ('contact_person_information', models.CharField(max_length=255)),
                ('customer_email', models.EmailField(max_length=254)),
                ('order_forms', models.FileField(upload_to='order_forms/')),
                ('order_forms_part_2', models.FileField(upload_to='order_forms/')),
                ('block_number', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('feedback', models.TextField()),
            ],
        ),
    ]
