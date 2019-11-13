# Generated by Django 2.2.7 on 2019-11-12 19:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=150, unique_for_date='publish')),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-publish'],
            },
        ),
    ]