from django.db import models


class Kind(models.Model):
    choise = (('кот', 'кот'), ('собака', 'собака'), ('птица', 'птица'), ('рептилия', 'рептилия'), ('грызун', 'грызун'))
    name = models.CharField(max_length=20, choices=choise)

    def __str__(self):
        return self.name


class Breed(models.Model):
    choise = (('сибирская', 'сибирская'), ('британская', 'британская'),
              ('лайка', 'лайка'), ('овчарка', 'овчарка'),
              ('попугай', 'попугай'), ('канарейка', 'канарейка'),
              ('черепаха', 'черепаха'), ('ящерица', 'ящерица'),
              ('хомяк', 'хомяк'), ('мышь', 'мышь'))
    name = models.CharField(max_length=50, choices=choise)
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Diagnosis(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Medicines(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=20)
    kind = models.ForeignKey(Kind, on_delete=models.SET_NULL, null=True)
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True)
    diag = models.ManyToManyField(Diagnosis, null=True)
    meds = models.ManyToManyField(Medicines, null=True)