# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porn', '0007_auto_20140925_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
