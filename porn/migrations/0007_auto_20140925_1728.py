# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porn', '0006_auto_20140925_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='country',
        ),
        migrations.DeleteModel(
            name='CountryCode',
        ),
        migrations.AddField(
            model_name='place',
            name='latitude',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='longitude',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
