# Generated by Django 3.1 on 2020-09-15 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivos', '0002_archivo_curso_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivo',
            name='des',
            field=models.CharField(default='Sin descripción', max_length=100),
        ),
    ]
