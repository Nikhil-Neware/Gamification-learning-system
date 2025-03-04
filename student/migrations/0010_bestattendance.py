# Generated by Django 3.2.13 on 2022-04-13 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_delete_flipped'),
        ('account', '0001_initial'),
        ('student', '0009_flipped'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staff')),
                ('staff_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_profile_best_attendance', to='account.profile')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
                ('student_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile_best_attendance', to='account.profile')),
            ],
            options={
                'db_table': 'best_attendance',
            },
        ),
    ]
