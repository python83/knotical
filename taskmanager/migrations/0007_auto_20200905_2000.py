# Generated by Django 3.1 on 2020-09-05 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0006_auto_20200905_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knotscategory',
            name='category_name',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
