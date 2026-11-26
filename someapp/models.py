from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class UserWithPhone(AbstractUser):
    phone = models.CharField(
        "Номер телефона",
        max_length=17,
    )

class Course(models.Model):
    title = models.CharField('Название курса', max_length=200)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', upload_to='courses/', blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    duration = models.CharField('Длительность', max_length=50)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title

class Request(models.Model):
    user = models.ForeignKey('UserWithPhone', on_delete=models.CASCADE) 
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    comment = models.TextField('Комментарий', blank=True)
    status = models.IntegerField('Статус', choices=[(0, 'Новая'), (1, 'Одобрена')], default=0)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'