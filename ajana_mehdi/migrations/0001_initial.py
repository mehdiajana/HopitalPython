# Generated by Django 4.0.3 on 2022-05-03 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medecin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=45)),
                ('prenom', models.CharField(max_length=45)),
                ('specialite', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=45)),
                ('prenom', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=100)),
                ('dateNaissance', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateRendezvous', models.DateField(null=True)),
                ('annuler', models.BooleanField(default=False)),
                ('medecin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ajana_mehdi.medecin')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ajana_mehdi.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=60)),
                ('rendezvous', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ajana_mehdi.rendezvous')),
            ],
        ),
    ]