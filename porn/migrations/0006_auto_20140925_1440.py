# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porn', '0005_auto_20140925_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='code',
        ),
        migrations.RemoveField(
            model_name='countrycode',
            name='occurances',
        ),
        migrations.AlterField(
            model_name='place',
            name='country',
            field=models.ForeignKey(to='porn.CountryCode'),
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
