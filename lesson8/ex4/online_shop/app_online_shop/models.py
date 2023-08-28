from django.db import models
from django.utils.html import format_html
from django.utils import timezone
from django.contrib import admin

# Create your models here.

# создаём класс с описанием структуры будущей таблицы (наследуемся от класса Model)
class OnlineShop(models.Model):
    # создаём заголовок объявления
    # CharField - класс, обозначающий символьное поле (набор символов), подходит для небольших текстов
    title = models.CharField('Заголовок', max_length=128)
    # создаём описание объявления
    # TextField - класс, обозначающий строковое поле больших размеров
    description = models.TextField('Описание')
    # создаём цену
    # Decimal - дробное число с фиксированной точностью (похоже на float в Python)
    # max_digits - максимальное количество цифр в числе
    # decimal_places - количество знаков после запятой
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    # создаём возможность торговаться
    # BooleanField - логический тип данных (истина или ложь)
    auction = models.BooleanField('Торг', help_text='Отметьте, уместен ли торг')
    # создаём дату размещения объявления
    # auto_now_add=True - сразу получаем дату в момент размещения объявления
    created_time = models.DateTimeField(auto_now_add=True)
    # создаём дату обновления объявления
    # auto_now=True - получаем дату в момент обновления объявления
    update_time = models.DateTimeField(auto_now=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_time.date() == timezone.now().date():
            created_time = self.created_time.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_time.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Дата последнего обновления')
    def updated_date(self):
        if self.update_time.date() == timezone.now().date():
            created_time = self.update_time.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.update_time.strftime("%d.%m.%Y в %H:%M:%S")

    class Meta:
        db_table = 'advertisements'
    
    def __str__(self):
        return f'OnlineShop(id={self.id}, title={self.title}, price={self.price})'