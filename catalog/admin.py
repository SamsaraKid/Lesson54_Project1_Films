from django.contrib import admin
from .models import *


admin.site.register(Diagnosis)
admin.site.register(Medicines)
admin.site.register(Doctor)


class Patientadmin(admin.ModelAdmin):
    list_display = ('name', 'kind', 'breed', 'diags')
    list_filter = ('kind', 'diag', 'meds', 'doc')
    fieldsets = (('Информация', {'fields': ('name', 'kind', 'breed')}),
                 ('Лечение', {'fields': ('doc', 'diag', 'meds')}))
admin.site.register(Patient, Patientadmin)


class Breedadmin(admin.ModelAdmin):
    list_display = ('name', 'kind')
admin.site.register(Breed, Breedadmin)


class Stinline(admin.TabularInline):
    model = Patient


class Kindadmin(admin.ModelAdmin):
    inlines = [Stinline]
admin.site.register(Kind, Kindadmin)

