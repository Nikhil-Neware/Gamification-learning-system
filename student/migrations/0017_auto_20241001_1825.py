# Generated by Django 3.2.13 on 2024-10-01 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_auto_20220523_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestperfomer',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='flipped',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='studentquizquestion',
            name='option',
            field=models.CharField(max_length=255),
        ),
    ]
