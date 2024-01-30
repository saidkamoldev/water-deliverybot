from django.db import models


class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(TimeBasedModel):
    class Meta:
        verbose_name = "Пользователь ",
        verbose_name_plural = "Пользователи "

    id = models.AutoField(primary_key=True)
    telegram_id = models.BigIntegerField(unique=True, default=1, verbose_name="ID пользователя Телеграм")
    name = models.CharField(max_length=255, verbose_name="Имя пользователя")
    username = models.CharField(max_length=255, verbose_name="Username Telegram")
    location = models.CharField(max_length=255, verbose_name="Локация")
    status = models.BooleanField(verbose_name="Статус анкеты", default=False)
    phone = models.CharField(max_length=200, verbose_name="Phone Number", null=True)
    language = models.CharField(max_length=10, verbose_name="Язык пользователя", null=True)

    # namecommand = models.CharField(max_length=200, verbose_name="Название Команды", null=True)

    def __str__(self):
        return f"№{self.id} ({self.telegram_id}) - {self.name}"



class Offer(TimeBasedModel):
    class Meta:
        verbose_name = "Заказ",
        verbose_name_plural = "Заказы "

    id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=255, verbose_name="Дата и время")
    telegram_id = models.CharField(max_length=255, verbose_name="Телеграм ID")
    username = models.CharField(max_length=255, verbose_name="Никнейм пользователя", null=True)
    status = models.CharField(max_length=255, verbose_name="Статус")
    product = models.CharField(max_length=255, verbose_name="Продукт")
    quantity = models.BigIntegerField(verbose_name="Количетсво", null=True)
    payment = models.CharField(max_length=255, verbose_name="Тип оплаты")
    price = models.CharField(max_length=255, verbose_name="Цена", null=True)
    commentary = models.CharField(max_length=255, verbose_name="Комементарии к заказу")


    def __str__(self):
        return f"№{self.id} ({self.category}) - {self.name}"
