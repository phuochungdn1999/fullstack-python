# Generated by Django 5.0.2 on 2024-03-01 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
                ('path', models.CharField(default='', max_length=200)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]