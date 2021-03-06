# Generated by Django 2.2.9 on 2019-12-19 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0004_facebookuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstargramUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_relation_set', to='many_to_many.InstargramUser')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_relation_set', to='many_to_many.InstargramUser')),
            ],
        ),
        migrations.AddField(
            model_name='instargramuser',
            name='following',
            field=models.ManyToManyField(through='many_to_many.Relation', to='many_to_many.InstargramUser'),
        ),
    ]
