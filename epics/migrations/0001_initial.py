# encoding: utf8
from django.db import models, migrations
from django.conf import settings
import django.contrib.gis.db.models.fields


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
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
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
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id', null=True)),
                ('title', models.CharField(max_length=64)),
                ('epic_num', models.CharField(max_length=6)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('description', models.TextField()),
                ('target_day', models.DateField()),
                ('target_time', models.DateTimeField()),
                ('public', models.BooleanField(default=False)),
                ('repeated', models.IntegerField(default=0, choices=((0, 'Daily'), (1, 'Weekly'), (2, 'Weekdays'), (3, 'MWF'), (4, 'TTh'), (5, 'Weekends'), (6, 'Monthly')))),
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
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id', null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
