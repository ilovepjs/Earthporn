# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porn', '0004_auto_20140925_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrycode',
            name='code',
            field=models.CharField(max_length=2, serialize=False, primary_key=True),
        ),
    ]
