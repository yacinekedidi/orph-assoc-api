# Generated by Django 3.1.2 on 2020-10-24 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mvpapp', '0010_auto_20201024_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orphaneducation',
            name='orphan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mvpapp.orphan', unique=True),
        ),
    ]
