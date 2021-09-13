from django.db import models


class Services(models.Model):
    name = models.TextField(
        max_length=255,
        verbose_name='Наименование услуги'
    )
    price = models.TextField(
        max_length=255,
        verbose_name='Стоимость услуги',
        default='-'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'


class Contact(models.Model):
    name = models.TextField(
        max_length=255,
        verbose_name='Имя контакта'
    )
    number = models.IntegerField(
        verbose_name='Номер телефона',
    )
    email = models.EmailField(
        verbose_name='EMAIL адрес'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class DefaultContact(models.Model):
    number = models.IntegerField(
        verbose_name='Номер телефона',
    )
    email = models.EmailField(
        verbose_name='EMAIL адрес'
    )
    address = models.TextField(
        verbose_name='Адрес'
    )

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = 'Основные Контакты'
        verbose_name_plural = 'Основные Контакты'
