# Generated by Django 2.2.16 on 2021-02-17 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('boards', '0002_auto_20210210_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts',
                                    to='boards.Topic'),
        ),
    ]
