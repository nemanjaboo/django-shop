# Generated by Django 4.1.3 on 2022-12-02 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_game_category_remove_game_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.IntegerField(),
        ),
    ]