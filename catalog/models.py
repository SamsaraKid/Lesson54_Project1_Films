from django.db import models
from django.urls import reverse


class Kind(models.Model):
    choise = (('кот', 'кот'), ('собака', 'собака'), ('птица', 'птица'), ('рептилия', 'рептилия'), ('грызун', 'грызун'))
    name = models.CharField(max_length=20, choices=choise, verbose_name='Вид')

    def __str__(self):
        return self.name


class Breed(models.Model):
    choise = (('сибирская', 'сибирская'), ('британская', 'британская'),
              ('лайка', 'лайка'), ('овчарка', 'овчарка'),
              ('попугай', 'попугай'), ('канарейка', 'канарейка'),
              ('черепаха', 'черепаха'), ('ящерица', 'ящерица'),
              ('хомяк', 'хомяк'), ('мышь', 'мышь'))
    name = models.CharField(max_length=50, choices=choise, verbose_name='Разновидность')
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE, verbose_name='Вид')

    def __str__(self):
        return self.name


class Diagnosis(models.Model):
    name = models.CharField(max_length=50, verbose_name='Диагноз')

    def __str__(self):
        return self.name


class Medicines(models.Model):
    name = models.CharField(max_length=50, verbose_name='Лекарства')

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=20, verbose_name='Врач')
    avatar = models.ImageField(upload_to='doctors/', blank=True, null=True)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=20, verbose_name='Кличка')
    kind = models.ForeignKey(Kind, on_delete=models.SET_NULL, null=True, verbose_name='Вид')
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True, verbose_name='Разновидность')
    diag = models.ManyToManyField(Diagnosis, null=True, verbose_name='Диагноз')
    meds = models.ManyToManyField(Medicines, null=True, verbose_name='Лекарства')
    doc = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, verbose_name='Врач')

    def __str__(self):
        return self.name

    def diags(self):
        return ', '.join([i.name for i in self.diag.all()])

    def medses(self):
        return ', '.join([i.name for i in self.meds.all()])

    def get_absolute_url(self):
        return reverse('medcard', args=[self.id])