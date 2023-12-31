# Generated by Django 4.2.7 on 2023-11-20 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarsListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Напишите название машины')),
                ('image', models.ImageField(upload_to='cars/', verbose_name='Добавьте фото')),
                ('year', models.DateField(verbose_name='Укажите год выпуска')),
                ('mark', models.CharField(choices=[('Mersedes', 'Mersedes'), ('BMW', 'BMW'), ('Honda', 'Honda')], max_length=100)),
                ('description', models.TextField(blank=True, verbose_name='Описание фильма')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
