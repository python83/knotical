# Generated by Django 3.1 on 2020-09-05 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0005_auto_20200903_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knotscategory',
            name='category_name',
            field=models.CharField(choices=[(0, 'No Textbox'), (1, 'One Textbox: ')], max_length=256, unique=True),
        ),
    ]
