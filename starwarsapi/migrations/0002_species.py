# Generated by Django 3.0.2 on 2020-02-03 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starwarsapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('classification', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
            ],
        ),
    ]
