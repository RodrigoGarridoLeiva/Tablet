# Generated by Django 3.0.3 on 2020-08-13 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_listaalumno'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='id_unico',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
