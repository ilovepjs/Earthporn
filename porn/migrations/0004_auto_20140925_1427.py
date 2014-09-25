# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porn', '0003_auto_20140925_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryCode',
            fields=[
                ('code', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('occurances', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.ForeignKey(to='porn.CountryCode'),
        ),
    ]
