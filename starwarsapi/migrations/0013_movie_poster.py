# Generated by Django 3.0.2 on 2020-02-04 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starwarsapi', '0012_character_sith_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
