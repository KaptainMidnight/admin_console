# Generated by Django 3.0.2 on 2020-01-11 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_auto_20200111_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.IntegerField(default=1, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='user',
            name='money',
            field=models.IntegerField(default=0, verbose_name='Баланс'),
        ),
    ]
