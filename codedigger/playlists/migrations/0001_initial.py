# Generated by Django 3.1.4 on 2020-12-12 13:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problemlists', '0002_auto_20201211_2246'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=100)),
                ('description', models.TextField(default=' ', max_length=200)),
                ('owner', models.ManyToManyField(related_name='Owner', to=settings.AUTH_USER_MODEL)),
                ('problems', models.ManyToManyField(related_name='Problem', to='problemlists.Problem')),
            ],
        ),
    ]
