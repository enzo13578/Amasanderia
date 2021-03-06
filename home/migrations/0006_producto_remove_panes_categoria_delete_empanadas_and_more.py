# Generated by Django 4.0.1 on 2022-05-19 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_usuario_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=30, verbose_name='Tipo Pan')),
                ('stock', models.IntegerField(max_length=10, verbose_name='Stock')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.categoria')),
            ],
        ),
        migrations.RemoveField(
            model_name='panes',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='empanadas',
        ),
        migrations.DeleteModel(
            name='panes',
        ),
    ]
