# Generated by Django 4.1.7 on 2023-03-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habit',
            options={'verbose_name': 'Привычка', 'verbose_name_plural': 'Привычки'},
        ),
        migrations.AlterField(
            model_name='habit',
            name='time_to_complete',
            field=models.TimeField(default='00:02', verbose_name='время на выполнение'),
        ),
    ]
