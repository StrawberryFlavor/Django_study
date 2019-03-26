# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wind_test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('heroname', models.CharField(max_length=20)),
                ('herogender', models.BooleanField(default=False)),
                ('herocomment', models.CharField(max_length=128)),
                ('herobook', models.ForeignKey(to='wind_test.BookInfo')),
            ],
        ),
    ]
