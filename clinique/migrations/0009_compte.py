# Generated by Django 5.0 on 2024-01-27 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinique', '0008_patient_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]