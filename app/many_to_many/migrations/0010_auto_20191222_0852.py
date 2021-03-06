# Generated by Django 2.2.9 on 2019-12-22 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0009_auto_20191222_0812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Webtoon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='many_to_many.Platform')),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('platforms', models.ManyToManyField(through='many_to_many.Webtoon', to='many_to_many.Platform')),
            ],
        ),
        migrations.AddField(
            model_name='webtoon',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='many_to_many.Writer'),
        ),
    ]
