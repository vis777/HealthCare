# Generated by Django 4.2.5 on 2023-11-02 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0004_replydb'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertdb',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
    ]
