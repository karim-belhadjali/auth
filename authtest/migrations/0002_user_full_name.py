# Generated by Django 3.1.2 on 2020-11-09 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
