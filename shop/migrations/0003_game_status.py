# Generated by Django 4.1.3 on 2022-11-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_game_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.BooleanField(default=0),
        ),
    ]
