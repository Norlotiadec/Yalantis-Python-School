from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название курса')
    content = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание курса')
    date_start = models.DateTimeField(verbose_name='Дата начала курса')
    date_end = models.DateTimeField(verbose_name='Дата окончания курса')
    amount_lecture = models.PositiveSmallIntegerField(verbose_name='Количество лекций')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
