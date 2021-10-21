# Generated by Django 3.2.8 on 2021-10-21 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cartas', '0007_delete_cartas_completas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartas_Completas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_carta', models.ImageField(blank=True, upload_to='Cartas_Completas')),
                ('cartas_jugador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cartas.carta')),
            ],
            options={
                'verbose_name': 'Cartas Completas',
                'verbose_name_plural': 'Cartas Completas',
            },
        ),
    ]
