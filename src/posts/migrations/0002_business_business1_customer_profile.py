# Generated by Django 3.1.2 on 2020-10-18 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=127)),
                ('first_name', models.CharField(default='', max_length=127)),
                ('middle_name', models.CharField(default='', max_length=127)),
                ('last_name', models.CharField(default='', max_length=127)),
                ('password', models.CharField(default='', max_length=127)),
                ('cellnumber', models.CharField(default='', max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('email', models.CharField(default='123@aol.com', max_length=127)),
                ('password', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(blank=True, max_length=31)),
                ('cell_number', models.CharField(max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Business1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=12)),
                ('store_name', models.CharField(blank=True, max_length=100)),
                ('store_number', models.CharField(blank=True, max_length=12)),
                ('store_address', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(default='Ny', max_length=30)),
                ('state', models.CharField(blank=True, max_length=2)),
                ('zipcode', models.CharField(blank=True, max_length=5)),
                ('input_sex', models.CharField(max_length=3, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
