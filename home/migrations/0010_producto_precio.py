# Generated by Django 4.0.4 on 2022-06-09 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_producto_nombreproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=100, verbose_name='Precio'),
            preserve_default=False,
        ),
    ]
