# Generated by Django 3.1.2 on 2020-11-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtest', '0003_auto_20201109_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='customer', max_length=200)),
            ],
        ),
    ]