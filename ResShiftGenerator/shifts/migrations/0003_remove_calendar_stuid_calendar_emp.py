#l Generated by Django 5.0 on 2024-01-03 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0002_calendar_stuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='stuID',
        ),
        migrations.AddField(
            model_name='calendar',
            name='emp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned', to='shifts.staff'),
        ),
    ]
