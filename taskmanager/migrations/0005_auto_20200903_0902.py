# Generated by Django 3.1 on 2020-09-03 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0004_auto_20200902_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knots',
            name='knot_title',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]