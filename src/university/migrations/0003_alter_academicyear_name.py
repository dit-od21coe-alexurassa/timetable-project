# Generated by Django 5.0 on 2023-12-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("university", "0002_lecturer_module_intakeclass_intakestream_timetable"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academicyear",
            name="name",
            field=models.CharField(
                help_text="Eg. 2023/24 or 2023/2024", max_length=9, unique=True
            ),
        ),
    ]
