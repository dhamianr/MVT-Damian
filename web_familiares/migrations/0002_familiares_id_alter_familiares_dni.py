# Generated by Django 4.0.3 on 2022-04-05 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_familiares', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiares',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='familiares',
            name='dni',
            field=models.IntegerField(),
        ),
    ]
