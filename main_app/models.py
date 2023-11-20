from django.db import models

class CarsListModel(models.Model):
    MARK = (
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('BMW', 'BMW'),
        ('Honda', 'Honda')
    )
    title = models.CharField(max_length=100, verbose_name='Напишите название машины')
    image = models.ImageField(upload_to='cars/', verbose_name='Добавьте фото')
    year = models.DateField(verbose_name='Укажите год выпуска')
    mark = models.CharField(max_length=100, choices=MARK)
    description = models.TextField(blank=True, verbose_name='Описание машины')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

class Afisha(models.Model):
    car = models.CharField(max_length=100, verbose_name='Название машины Афиша')
    drive = models.PositiveIntegerField(verbose_name='Пробег машины в км')
    cost = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.car

class Slider(models.Model):
    slide = models.URLField()

    def __str__(self):
        return self.slide