# Generated by Django 4.0.3 on 2022-04-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_weather_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='lat',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='city',
            name='long',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
