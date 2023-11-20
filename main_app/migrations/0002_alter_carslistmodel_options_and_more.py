# Generated by Django 4.2.7 on 2023-11-20 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carslistmodel',
            options={'verbose_name': 'Машина', 'verbose_name_plural': 'Машины'},
        ),
        migrations.AlterField(
            model_name='carslistmodel',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание машины'),
        ),
        migrations.AlterField(
            model_name='carslistmodel',
            name='mark',
            field=models.CharField(choices=[('Mercedes-Benz', 'Mercedes-Benz'), ('BMW', 'BMW'), ('Honda', 'Honda')], max_length=100),
        ),
    ]