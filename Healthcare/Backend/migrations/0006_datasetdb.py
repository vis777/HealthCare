# Generated by Django 4.2.5 on 2023-11-02 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0005_expertdb_is_blocked'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatasetDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(blank=True, max_length=100, null=True)),
                ('Answer', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
