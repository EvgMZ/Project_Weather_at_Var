# Generated by Django 4.0.3 on 2022-04-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='temperature',
            field=models.CharField(max_length=150),
        ),
    ]
