# Generated by Django 2.2.12 on 2020-04-06 13:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20200406_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
