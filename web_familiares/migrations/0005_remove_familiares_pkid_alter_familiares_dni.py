# Generated by Django 4.0.3 on 2022-04-05 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_familiares', '0004_rename_id_familiares_pkid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiares',
            name='pkid',
        ),
        migrations.AlterField(
            model_name='familiares',
            name='dni',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]