# Generated by Django 3.2.13 on 2023-11-19 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_moviereview_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviereview',
            name='rank',
            field=models.IntegerField(),
        ),
    ]