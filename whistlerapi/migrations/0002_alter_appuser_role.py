# Generated by Django 4.0.3 on 2022-03-13 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whistlerapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role', to='whistlerapi.role'),
        ),
    ]
