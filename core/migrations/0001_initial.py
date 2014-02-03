# encoding: utf8
from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):
    
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EpicUser',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name=u'password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name=u'last login')),
                ('email', models.EmailField(unique=True, max_length=255)),
                ('first_name', models.CharField(max_length=64, null=True)),
                ('last_name', models.CharField(max_length=64, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                u'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
