# encoding: utf8
from django.db import models, migrations
import django.contrib.gis.db.models.fields
from django.conf import settings


class Migration(migrations.Migration):
    
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_id', models.CharField(max_length=128, db_index=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(default='POINT(0.0 0.0)', srid=4326, verbose_name='Point')),
                ('connected', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Epic',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('epic_uuid', models.CharField(max_length=64)),
                ('organizer_id', models.CharField(max_length=128)),
                ('user', models.ForeignKey(to_field=u'id', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('title', models.CharField(max_length=64)),
                ('epic_num', models.CharField(max_length=6)),
                ('location', django.contrib.gis.db.models.fields.PointField(default='POINT(0.0 0.0)', srid=4326, verbose_name='Point')),
                ('description', models.TextField()),
                ('target_day', models.DateField()),
                ('target_time', models.DateTimeField()),
                ('public', models.BooleanField(default=False)),
                ('repeated', models.IntegerField(default=0, choices=((0, 'One Time'), (1, 'Daily'), (2, 'Weekly'), (3, 'Weekdays'), (4, 'MWF'), (5, 'TTh'), (6, 'Weekends'), (7, 'Monthly')))),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EpicSubscription',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('epic', models.ForeignKey(to='epics.Epic', to_field=u'id')),
                ('participant_id', models.CharField(max_length=128, db_index=True)),
                ('user', models.ForeignKey(to_field=u'id', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('join_location', django.contrib.gis.db.models.fields.PointField(default='POINT(0.0 0.0)', srid=4326, verbose_name='Point')),
                ('leave', models.DateTimeField(default=None, null=True, blank=True)),
                ('leave_location', django.contrib.gis.db.models.fields.PointField(default='POINT(0.0 0.0)', srid=4326, verbose_name='Point')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
