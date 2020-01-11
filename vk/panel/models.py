from django.db import models


class User(models.Model):
    """
    Модель для пользователей
    """
    external_id = models.IntegerField(
        verbose_name='Внешний ID',
    )
    money = models.IntegerField(
        verbose_name='Баланс',
        default=0,
    )
    level = models.IntegerField(
        verbose_name='Уровень',
        default=1
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
