# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porn', '0009_place_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country', models.CharField(max_length=400, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='place',
            name='country',
            field=models.ForeignKey(to='porn.Country'),
        ),
    ]
