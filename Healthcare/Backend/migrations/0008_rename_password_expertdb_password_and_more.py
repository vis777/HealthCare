# Generated by Django 4.2.5 on 2023-11-14 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0007_homeremedydb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expertdb',
            old_name='PassWord',
            new_name='PassWoRd',
        ),
        migrations.RenameField(
            model_name='expertdb',
            old_name='UserName',
            new_name='UserNaMe',
        ),
    ]
