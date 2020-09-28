# Generated by Django 2.2 on 2020-09-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silk', '0007_sqlquery_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='username',
            field=models.CharField(db_index=True, default='guest', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='response',
            name='username',
            field=models.CharField(db_index=True, default='guest', max_length=100),
            preserve_default=False,
        ),
    ]
