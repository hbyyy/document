# Generated by Django 2.2.9 on 2019-12-22 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0010_auto_20191222_0852'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='platform',
            table='m2m_platform',
        ),
        migrations.AlterModelTable(
            name='webtoon',
            table='m2m_webtoon',
        ),
        migrations.AlterModelTable(
            name='writer',
            table='m2m_writer',
        ),
    ]
