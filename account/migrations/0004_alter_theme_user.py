# Generated by Django 4.1 on 2022-08-31 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]