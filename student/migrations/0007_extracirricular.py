# Generated by Django 3.2.11 on 2022-02-28 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_attendance'),
        ('account', '0001_initial'),
        ('student', '0006_studentattendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraCirricular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_type', models.CharField(max_length=50)),
                ('coin', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now=True)),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.attendance')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staff')),
                ('staff_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_profile_extra', to='account.profile')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
                ('student_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile_extra', to='account.profile')),
            ],
            options={
                'db_table': 'extra_circullar',
            },
        ),
    ]
