# Generated by Django 4.0.1 on 2022-05-12 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='panes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoPan', models.CharField(max_length=30, verbose_name='Tipo Pan')),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.categoria')),
            ],
        ),
    ]