# Generated by Django 3.2.5 on 2021-08-04 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewapp', '0002_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='d_date',
            new_name='d_day',
        ),
    ]