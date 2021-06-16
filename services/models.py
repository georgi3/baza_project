from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.deletion import CASCADE
from django.core.exceptions import ValidationError


class Rooms(models.Model):
    name = models.CharField('Название', max_length=20)
    price = models.IntegerField('Цена')
    kitchen = models.CharField('Есть ли Кухня', max_length=20, blank=True, null=True)
    washroom = models.IntegerField('Кол. туалетов', blank=True, null=True)
    places = models.IntegerField('Кол. спальных мест')
    rooms = models.IntegerField('Кол. комнат', blank=True, null=True)
    pool = models.CharField('Есть ли бильярд', max_length=20, blank=True)
    # Add file check constraints for imgs
    img = models.ImageField(upload_to='photos/rooms/')
    img1 = models.ImageField(upload_to='photos/rooms/', blank=True, null=True)
    img2 = models.ImageField(upload_to='photos/rooms/', blank=True, null=True)
    img3 = models.ImageField(upload_to='photos/rooms/', blank=True, null=True)
    img4 = models.ImageField(upload_to='photos/rooms/', blank=True, null=True)
    img5 = models.ImageField(upload_to='photos/rooms/', blank=True, null=True)
    img6 = models.ImageField(upload_to='photos/rooms/', blank=True, null=True)
    img7 = models.ImageField(upload_to='photos/rooms/', blank=True, null=True)

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'


class Booking(models.Model):
    first_name = models.CharField('Имя', max_length=20, null=True)
    last_name = models.CharField('Фамилия', max_length=20, null=True)
    email = models.EmailField("Почта")
    phone = PhoneNumberField('Телефон', null=True)
    choice = models.CharField('Выбор Жилья', max_length=30)
    starting_date = models.DateField('Начало')
    end_date = models.DateField('Конец')
    total_sum = models.IntegerField('Сума Оплаты', null=True)

    # Maybe add card number or account depending on the type of payment
    # Add total amount
    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'

    def dates_check(self, starting_date, ending_date):
        pass




