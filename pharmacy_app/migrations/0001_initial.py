# Generated by Django 4.1.7 on 2023-04-17 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveBigIntegerField(default=0)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('postalCode', models.PositiveIntegerField(default=1000, unique=True)),
                ('country', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Address',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(default=0, primary_key=True, serialize=False)),
                ('firstName', models.CharField(default='', max_length=100)),
                ('lastName', models.CharField(default='', max_length=100)),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('speciality', models.CharField(choices=[('Cardiologist', 'Cardiologist specialty'), ('Dermatologist', 'Dermatologist specialty')], default='Cardiologist', max_length=100)),
            ],
            options={
                'db_table': 'Doctor',
            },
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('manufacturingDate', models.DateField(blank=True, null=True)),
                ('expirationDate', models.DateField(blank=True, null=True)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos')),
            ],
            options={
                'db_table': 'Drug',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(default=0, primary_key=True, serialize=False)),
                ('firstName', models.CharField(default='', max_length=100)),
                ('lastName', models.CharField(default='', max_length=100)),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'Patient',
                'ordering': ['-lastName', '-email'],
            },
        ),
    ]
