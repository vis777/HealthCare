# Generated by Django 4.2.5 on 2023-10-31 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_rename_area_expertdb_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DName', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
