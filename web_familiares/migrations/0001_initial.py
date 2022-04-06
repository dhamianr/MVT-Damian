# Generated by Django 4.0.3 on 2022-04-03 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('nombres', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=20)),
                ('dni', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]