# Generated by Django 2.2.9 on 2019-12-19 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, verbose_name='주소')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='상점명')),
                ('type', models.CharField(choices=[('convenience', '편의점'), ('game', '게임샵')], max_length=30, verbose_name='상점유형')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='식당명')),
                ('rating', models.IntegerField(default=0, verbose_name='평점')),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='one_to_one.Place', verbose_name='장소')),
            ],
        ),
    ]
