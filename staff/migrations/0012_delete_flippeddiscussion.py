# Generated by Django 5.1.6 on 2025-02-25 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0011_rename_is_resolved_flippeddiscussion_resolve'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FlippedDiscussion',
        ),
    ]
