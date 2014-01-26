# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Epic',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('epic_uuid', models.CharField(max_length=64)),
                ('epic_num', models.CharField(max_length=6)),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('target_day', models.DateField()),
                ('target_time', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
