# Generated by Django 3.1.2 on 2020-10-26 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0034_remove_business_input_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='password1',
        ),
    ]