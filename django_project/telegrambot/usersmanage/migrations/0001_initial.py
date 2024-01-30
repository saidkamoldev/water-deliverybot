# Generated by Django 4.1.4 on 2023-10-05 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=255, verbose_name='Дата и время')),
                ('telegram_id', models.CharField(max_length=255, verbose_name='Телеграм ID')),
                ('username', models.CharField(max_length=255, null=True, verbose_name='Никнейм пользователя')),
                ('status', models.CharField(max_length=255, verbose_name='Статус')),
                ('product', models.CharField(max_length=255, verbose_name='Продукт')),
                ('quantity', models.BigIntegerField(null=True, verbose_name='Количетсво')),
                ('payment', models.CharField(max_length=255, verbose_name='Тип оплаты')),
                ('price', models.CharField(max_length=255, null=True, verbose_name='Цена')),
                ('commentary', models.CharField(max_length=255, verbose_name='Комементарии к заказу')),
            ],
            options={
                'verbose_name': ('Заказ',),
                'verbose_name_plural': 'Заказы ',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('telegram_id', models.BigIntegerField(default=1, unique=True, verbose_name='ID пользователя Телеграм')),
                ('name', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('username', models.CharField(max_length=255, verbose_name='Username Telegram')),
                ('location', models.CharField(max_length=255, verbose_name='Локация')),
                ('status', models.BooleanField(default=False, verbose_name='Статус анкеты')),
                ('phone', models.CharField(max_length=200, null=True, verbose_name='Phone Number')),
                ('language', models.CharField(max_length=10, null=True, verbose_name='Язык пользователя')),
            ],
            options={
                'verbose_name': ('Пользователь ',),
                'verbose_name_plural': 'Пользователи ',
            },
        ),
    ]
