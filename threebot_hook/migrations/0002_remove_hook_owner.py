# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threebot_hook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hook',
            name='owner',
        ),
    ]
