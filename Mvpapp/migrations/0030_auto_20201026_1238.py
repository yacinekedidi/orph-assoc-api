# Generated by Django 3.1.2 on 2020-10-26 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mvpapp', '0029_auto_20201026_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orphaneducation',
            name='orphan_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orphan_education', to='Mvpapp.orphan'),
        ),
    ]
