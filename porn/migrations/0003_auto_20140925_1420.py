# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porn', '0002_country_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='id',
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.CharField(max_length=400, serialize=False, primary_key=True),
        ),
    ]
