# Generated by Django 3.2.11 on 2022-01-14 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_quiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizQA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option_1', models.TextField()),
                ('option_2', models.TextField()),
                ('option_3', models.TextField()),
                ('option_4', models.TextField()),
                ('right_option', models.TextField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.quiz')),
            ],
            options={
                'db_table': 'quiz_qas',
            },
        ),
    ]
