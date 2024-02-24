from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.conf import settings
import pytz


class Period(models.Model):
    singular = models.CharField(max_length=6, verbose_name="Единственное число (1 час)")
    plural = models.CharField(max_length=6, verbose_name="Множественное число (2 часа)")
    plural_special = models.CharField(max_length=6, verbose_name="Множественное число дополнительное (30 часов)")

    def pluralize(self, count):
        if count % 10 == 1 and count % 100 != 11:
            return self.singular
        elif 2 <= count % 10 <= 4 and (count % 100 < 10 or count % 100 >= 20):
            return self.plural
        else:
            return self.plural_special

    def __str__(self):
        return self.singular

    class Meta:
        verbose_name = 'Период'
        verbose_name_plural = 'Периоды'


class AdditionalInfo(models.Model):
    displayed_name = models.CharField(
        verbose_name='Отображаемое название',
        max_length=100,
        help_text='Название, которое будет отображаться на сайте',
        default='Доп. информация')
    inner_name = models.CharField(
        verbose_name='Название',
        max_length=100,
        help_text='Это название уже для вашего удобства, оно отображается здесь, в админке',
        default='Доп. информация')

    def get_unique_name(self):
        return "additinal_info" + str(self.id)

    class Meta:
        verbose_name = 'Дополнительная информация'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.inner_name


class AdditionalInfoItem(models.Model):
    text = models.CharField(verbose_name="Текст", max_length=500)
    additional_info = models.ForeignKey(AdditionalInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункты'


class Attachment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def get_upload_path(self, filename):
        return f'landing/{self.content_type.name}_{self.object_id}/{filename}'

    def get_miniature_upload_path(self, filename):
        return f'landing/mini/{self.content_type.name}_{self.object_id}/{filename}'

    file = models.FileField("Фото/Видео", upload_to=get_upload_path)
    miniature = models.FileField(
        "Миниатюра (опционально)",
        upload_to=get_miniature_upload_path,
        null=True,
        blank=True,
        help_text='Изображение, чье разрешение должно быть приближено к 420х300, но не меньше. ' +
                  'Опционально, но так сайт будет грузиться быстрее')
    order = models.PositiveIntegerField("Порядок отображения", default=0, db_index=True)

    def is_video(self):
        return self.file.name.endswith('.mp4')

    def get_miniature_or_original(self):
        if self.miniature:
            return self.miniature.url

        return self.file.url

    def __str__(self):
        return self.file.name

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
        verbose_name = 'Фото/Видео'
        verbose_name_plural = verbose_name
        ordering = ['order']


class House(models.Model):
    name = models.CharField(verbose_name='Название', max_length=32)
    start_price = models.PositiveIntegerField(verbose_name='Начальная цена', help_text="Поставьте 0 если это бесплатно")
    duration = models.PositiveIntegerField(
        verbose_name='Продолжительность',
        default=1,
        validators=[MinValueValidator(1)])
    period = models.ForeignKey(Period, verbose_name='Период', default=1, on_delete=models.SET_DEFAULT)
    description = models.TextField(verbose_name='Описание', max_length=400)
    additional_info = models.ForeignKey(
        AdditionalInfo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Доп. информация',
        help_text='Добавляется в конец описания и открывается отдельном окном при нажатии')

    order = models.PositiveIntegerField("Порядок отображения", default=0, db_index=True)

    media = GenericRelation(Attachment)

    def get_pluralized_period(self):
        return self.period.pluralize(self.duration)

    def get_unique_name(self):
        return self.name + str(self.id)

    def get_duration_if_it_gte_1(self):
        if self.duration <= 1:
            return ""
        return str(self.duration) + " "

    def is_free(self):
        return self.start_price <= 0

    class Meta:
        verbose_name = 'Домик'
        verbose_name_plural = 'Домики'
        ordering = ['order']

    def __str__(self):
        return self.name


class WellnessTreatment(models.Model):
    name = models.CharField(verbose_name='Название', max_length=32)
    start_price = models.PositiveIntegerField(verbose_name='Начальная цена', help_text="Оставьте 0 если это бесплатно")
    duration = models.PositiveIntegerField(
        verbose_name='Продолжительность',
        default=1,
        validators=[MinValueValidator(1)])
    period = models.ForeignKey(Period, verbose_name='Период', default=1, on_delete=models.SET_DEFAULT)
    description = models.TextField(verbose_name='Описание', max_length=400)
    additional_info = models.ForeignKey(
        AdditionalInfo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Доп. информация',
        help_text='Добавляется в конец описания и открывается отдельном окном при нажатии')
    order = models.PositiveIntegerField("Порядок отображения", default=0, db_index=True)

    media = GenericRelation(Attachment)

    def get_pluralized_period(self):
        return self.period.pluralize(self.duration)

    def get_unique_name(self):
        return self.name + str(self.id)

    def get_duration_if_it_gte_1(self):
        if self.duration <= 1:
            return ""
        return str(self.duration) + " "

    def is_free(self):
        return self.start_price <= 0

    class Meta:
        verbose_name = 'Оздоровительная процедура'
        verbose_name_plural = 'Оздоровительные процедуры'
        ordering = ['order']

    def __str__(self):
        return self.name


class Action(models.Model):
    name = models.CharField(verbose_name='Название', max_length=32)
    start_price = models.PositiveIntegerField(verbose_name='Начальная цена', help_text="Оставьте 0 если это бесплатно")
    duration = models.PositiveIntegerField(
        verbose_name='Продолжительность / кол-во',
        default=1,
        validators=[MinValueValidator(1)])
    period = models.ForeignKey(Period, verbose_name='Период', default=1, on_delete=models.SET_DEFAULT)
    description = models.TextField(verbose_name='Описание', max_length=400)
    additional_info = models.ForeignKey(
        AdditionalInfo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Доп. информация',
        help_text='Добавляется в конец описания и открывается отдельном окном при нажатии')
    order = models.PositiveIntegerField("Порядок отображения", default=0, db_index=True)

    media = GenericRelation(Attachment)

    def get_pluralized_period(self):
        return self.period.pluralize(self.duration)

    def get_unique_name(self):
        return self.name + str(self.id)

    def get_duration_if_it_gte_1(self):
        if self.duration <= 1:
            return ""
        return str(self.duration) + " "

    def is_free(self):
        return self.start_price <= 0

    class Meta:
        verbose_name = 'Досуг'
        verbose_name_plural = 'Досуг'
        ordering = ['order']

    def __str__(self):
        return self.name


MEASURE_CHOICES = {
    ('кг', 'килограмм'),
    ('шт', 'штука'),
    ('л', 'литр'),
    ('г', 'грамм')
}


class OurProduct(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=500, blank=True, null=True)

    price = models.PositiveIntegerField('Стоимость')
    count = models.PositiveIntegerField('Кол-во', default=1)
    measure = models.CharField("Ед. измерения", choices=MEASURE_CHOICES, max_length=4, default=('шт', 'штука'))
    is_available = models.BooleanField("В наличии", default=True)

    media = GenericRelation(Attachment)

    def get_unique_name(self):
        return self.name + str(self.id)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = verbose_name
        ordering = ['-is_available', 'price']


class Event(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    date = models.DateTimeField("Дата и время")
    media = GenericRelation(Attachment)

    @admin.display(boolean=True, description='Прошло')
    def is_passed(self):
        return timezone.now() >= self.date

    def get_unique_name(self):
        return self.title + str(self.id)

    def __str__(self):
        datetime = self.date.astimezone(pytz.timezone(settings.TIME_ZONE)).strftime("%d.%m.%Y %H:%M")
        return f'{self.title} - {datetime}'

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['date']


class News(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    date = models.DateTimeField("Дата и время", auto_now_add=True)
    media = GenericRelation(Attachment)

    def get_unique_name(self):
        return self.title + str(self.id)

    def __str__(self):
        datetime = self.date.astimezone(pytz.timezone(settings.TIME_ZONE)).strftime("%d.%m.%Y")
        return f'{self.title} - {datetime}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date']
