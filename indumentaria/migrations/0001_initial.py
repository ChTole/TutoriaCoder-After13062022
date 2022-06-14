# Generated by Django 4.0.5 on 2022-06-13 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Remera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30, verbose_name='Marca')),
                ('talle', models.PositiveSmallIntegerField(choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL'), (6, 'XXL')], verbose_name='Talle')),
                ('color', models.CharField(max_length=15, verbose_name='Color')),
                ('precio', models.FloatField(verbose_name='Precio $')),
            ],
        ),
    ]
