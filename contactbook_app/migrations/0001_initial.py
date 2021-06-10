# Generated by Django 3.2.4 on 2021-06-10 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], default='f', max_length=1)),
                ('name', models.CharField(max_length=125)),
                ('firstname', models.CharField(max_length=125)),
                ('birthdate', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('address', models.CharField(max_length=225)),
                ('email', models.EmailField(blank=True, max_length=225)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], default='f', max_length=1)),
                ('name', models.CharField(max_length=125)),
                ('firstname', models.CharField(max_length=125)),
                ('birthdate', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('lastname', models.CharField(max_length=125)),
                ('job', models.CharField(blank=True, max_length=125)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
