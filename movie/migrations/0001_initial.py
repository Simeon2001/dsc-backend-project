# Generated by Django 3.0.7 on 2020-11-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='toplist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=15)),
                ('pics_url', models.CharField(max_length=1000)),
                ('year', models.IntegerField(default=20)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
