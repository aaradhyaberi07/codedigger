# Generated by Django 3.1.4 on 2020-12-11 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('prob_id', models.CharField(default='', max_length=500)),
                ('url', models.CharField(default='', max_length=500)),
                ('tags', models.CharField(default='', max_length=500)),
                ('contest_id', models.CharField(default='', max_length=100)),
                ('index', models.CharField(default='', max_length=5)),
                ('rating', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProbPreCreatedList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='', max_length=500)),
                ('ladder', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Solved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solved', models.BooleanField(default=False)),
            ],
        ),
    ]
