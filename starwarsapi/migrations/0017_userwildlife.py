# Generated by Django 3.0.2 on 2020-02-05 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starwarsapi', '0016_usercharacter_userplanet_wildlife'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWildlife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('classification', models.CharField(blank=True, max_length=200, null=True)),
                ('habitat', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
