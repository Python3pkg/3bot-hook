# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threebot', '__first__'),
        ('organizations', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=255)),
                ('user', models.CharField(max_length=255, null=True, blank=True)),
                ('repo', models.CharField(max_length=255, null=True, blank=True)),
                ('secret', models.CharField(max_length=255, null=True, blank=True)),
                ('owner', models.ForeignKey(blank=True, to='organizations.Organization', null=True)),
                ('param_list', models.ForeignKey(to='threebot.ParameterList')),
                ('worker', models.ForeignKey(to='threebot.Worker')),
                ('workflow', models.ForeignKey(to='threebot.Workflow')),
            ],
            options={
                'db_table': 'threebot_hook',
                'verbose_name': 'Hook',
                'verbose_name_plural': 'Hooks',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='hook',
            unique_together=set([('workflow', 'worker', 'param_list')]),
        ),
    ]
