# Generated by Django 4.0.2 on 2022-03-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(max_length=25)),
                ('phonenumber', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
