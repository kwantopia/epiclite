# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('epics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='epic',
            name='country',
            field=models.CharField(max_length=64, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='epic',
            name='address',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='epic',
            name='city',
            field=models.CharField(max_length=64, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='epic',
            name='zipcode',
            field=models.CharField(max_length=16, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='epic',
            name='state',
            field=models.CharField(max_length=64, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='epic',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
