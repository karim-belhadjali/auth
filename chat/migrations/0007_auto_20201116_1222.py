# Generated by Django 3.1.2 on 2020-11-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20201115_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
