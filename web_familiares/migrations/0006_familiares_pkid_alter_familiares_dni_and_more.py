# Generated by Django 4.0.3 on 2022-04-05 22:39

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web_familiares', '0005_remove_familiares_pkid_alter_familiares_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiares',
            name='pkid',
            field=models.AutoField(default=django.utils.timezone.now, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='familiares',
            name='dni',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='familiares',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, default=datetime.date, null=True),
        ),
    ]
