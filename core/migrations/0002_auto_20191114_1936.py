# Generated by Django 2.2.6 on 2019-11-14 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='anio',
            field=models.IntegerField(verbose_name='Año'),
        ),
    ]
