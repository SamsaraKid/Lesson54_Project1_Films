# Generated by Django 4.2.5 on 2023-09-26 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Врач')),
            ],
        ),
        migrations.AlterField(
            model_name='breed',
            name='kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.kind', verbose_name='Вид'),
        ),
        migrations.AlterField(
            model_name='breed',
            name='name',
            field=models.CharField(choices=[('сибирская', 'сибирская'), ('британская', 'британская'), ('лайка', 'лайка'), ('овчарка', 'овчарка'), ('попугай', 'попугай'), ('канарейка', 'канарейка'), ('черепаха', 'черепаха'), ('ящерица', 'ящерица'), ('хомяк', 'хомяк'), ('мышь', 'мышь')], max_length=50, verbose_name='Разновидность'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Диагноз'),
        ),
        migrations.AlterField(
            model_name='kind',
            name='name',
            field=models.CharField(choices=[('кот', 'кот'), ('собака', 'собака'), ('птица', 'птица'), ('рептилия', 'рептилия'), ('грызун', 'грызун')], max_length=20, verbose_name='Вид'),
        ),
        migrations.AlterField(
            model_name='medicines',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Лекарства'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='breed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.breed', verbose_name='Разновидность'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='diag',
            field=models.ManyToManyField(null=True, to='catalog.diagnosis', verbose_name='Диагноз'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='kind',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.kind', verbose_name='Вид'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='meds',
            field=models.ManyToManyField(null=True, to='catalog.medicines', verbose_name='Лекарства'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Кличка'),
        ),
        migrations.AddField(
            model_name='patient',
            name='doc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.doctor', verbose_name='Врач'),
        ),
    ]
