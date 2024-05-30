# Generated by Django 5.0.6 on 2024-05-30 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='Imagen')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
            ],
        ),
    ]