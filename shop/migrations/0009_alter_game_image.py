# Generated by Django 4.1.3 on 2022-12-05 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_game_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.URLField(),
        ),
    ]