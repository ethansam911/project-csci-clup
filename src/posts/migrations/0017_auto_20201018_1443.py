# Generated by Django 3.1.2 on 2020-10-18 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_auto_20201018_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='is_business',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='business',
            name='is_customer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='is_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='is_customer',
            field=models.BooleanField(default=True),
        ),
    ]
