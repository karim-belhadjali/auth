# Generated by Django 3.1.2 on 2020-11-09 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtest', '0004_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authtest.role'),
        ),
    ]
