# Generated by Django 5.1.6 on 2025-02-20 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='is_on_vacation',
            field=models.BooleanField(default=False),
        ),
    ]
