# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 12:08
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sounds', '0026_auto_20180404_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulkuploadprogress',
            name='description_output',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='bulkuploadprogress',
            name='progress_type',
            field=models.CharField(choices=[(b'N', b'Not yet validated'), (b'E', b'Errors ocurred'), (b'F', b'Finished'), (b'S', b'Sounds being described and processed'), (b'V', b'Finished validation.')], default=b'N', max_length=1),
        ),
    ]