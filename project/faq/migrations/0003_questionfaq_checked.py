# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_auto_20150607_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionfaq',
            name='checked',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
