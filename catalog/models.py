from django.db import models


class Kind(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=50)
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
    diag = models.ManyToManyField(Diagnosis, on_delete=models.SET_NULL, null=True)
    meds = models.ManyToManyField(Medicines, on_delete=models.SET_NULL, null=True)