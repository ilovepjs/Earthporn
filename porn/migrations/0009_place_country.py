# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porn', '0008_auto_20140925_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='country',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
    ]
