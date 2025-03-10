# Generated by Django 5.1.3 on 2024-12-03 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=200)),
                ('emp_id', models.CharField(max_length=200)),
                ('emp_age', models.IntegerField(max_length=10)),
                ('emp_phone_no', models.CharField(max_length=10)),
                ('emp_address', models.CharField(max_length=150)),
                ('emp_working', models.BooleanField(default=True)),
                ('emp_department', models.CharField(max_length=10)),
            ],
        ),
    ]
