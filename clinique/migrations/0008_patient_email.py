# Generated by Django 5.0 on 2024-01-27 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinique', '0007_patient_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
