# Generated by Django 3.1.4 on 2020-12-12 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201212_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='atcoder',
            field=models.CharField(blank=True, default='empty', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='codechef',
            field=models.CharField(blank=True, default='empty', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='spoj',
            field=models.CharField(blank=True, default='empty', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='uva_handle',
            field=models.CharField(blank=True, default='empty', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='uva_id',
            field=models.CharField(blank=True, default='empty', max_length=50, null=True),
        ),
    ]
