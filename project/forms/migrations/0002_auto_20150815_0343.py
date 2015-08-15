# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biblescool',
            name='rules',
            field=models.BooleanField(verbose_name='\u042f \u043f\u043e\u043d\u0438\u043c\u0430\u044e, \u0447\u0442\u043e, \u043a\u0430\u043a \u0441\u043b\u0443\u0448\u0430\u0442\u0435\u043b\u044c \u0411\u0438\u0431\u043b\u0435\u0439\u0441\u043a\u0438\u0445 \u043a\u0443\u0440\u0441\u043e\u0432, \u044f \u043e\u0431\u044f\u0437\u0430\u043d \u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u044c \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u043d\u044b\u043c \u043f\u0440\u0430\u0432\u0438\u043b\u0430\u043c.'),
            preserve_default=True,
        ),
    ]
