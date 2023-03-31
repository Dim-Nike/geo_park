from django.db import models
from django.contrib.auth.models import User


class GeneralUser(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(verbose_name='Номер телефона', max_length=11)
    is_active = models.IntegerField(verbose_name='Количество запросов', default=10)
    is_ban = models.BooleanField(verbose_name='Активный')


class SubUser(models.Model):
    SUBSCRIPTION_FIELDS = [
        ('1', 'Начинающий тариф'),
        ('2', 'Оптимальный тариф'),
        ('3', 'Продвинутый тариф'),
    ]

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(verbose_name='Номер телефона', max_length=11)
    is_active = models.IntegerField(verbose_name='Количество запросов', default=10)
    is_ban = models.BooleanField(verbose_name='Активный')
    subscription = models.CharField(verbose_name='Подписка', choices=SUBSCRIPTION_FIELDS, max_length=1, default='2')
    start_time_sub = models.DateTimeField(verbose_name='Дата последнего платежа')
    end_time_sub = models.DateTimeField(verbose_name='Дата окончания подписки')
    is_sub = models.BooleanField(verbose_name='Активность подписки')


class EditImage(models.Model):
    user_general = models.ForeignKey(verbose_name='Гость', on_delete=models.CASCADE, to=GeneralUser,
                                     blank=True, null=True)
    user_sub = models.ForeignKey(verbose_name='Пользователь с подпиской', on_delete=models.CASCADE, to=SubUser,
                                 blank=True, null=True)
    image_user = models.ImageField(verbose_name='Фотография пользователя', upload_to='photo/image_user/%Y/%m/%d/')
    image_neural = models.ImageField(verbose_name='Обработанная фотография', upload_to='photo/image_user/%Y/%m/%d/',
                                     blank=True, null=True)
    desc = models.TextField(verbose_name='Описание к изображению', blank=True, null=True)
    is_done = models.BooleanField(verbose_name='Обработанный заказ', default=False)


class CategoriesNews(models.Model):
    name = models.CharField(verbose_name='Наименование категории', max_length=155)
    photo = models.ImageField(verbose_name='Фотография', upload_to='photo/information/categories/%Y/%m/%d/')
    is_active = models.BooleanField(verbose_name='Активный', default=False)


class News(models.Model):
    categories = models.ForeignKey(to=CategoriesNews, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    photo = models.ImageField(verbose_name='Фотография', upload_to='photo/information/news/%Y/%m/%d/')
    desc = models.TextField(verbose_name='Контент')
    is_active = models.BooleanField(verbose_name='Активный', default=True)

