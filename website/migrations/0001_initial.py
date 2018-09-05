# Generated by Django 2.1 on 2018-08-08 18:58

from django.db import migrations, models
import s3direct.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('team', models.CharField(max_length=150)),
                ('event_name', models.CharField(blank=True, max_length=500)),
                ('position', models.CharField(max_length=5)),
                ('college_name', models.CharField(max_length=10)),
                ('fest_name', models.CharField(blank=True, max_length=100)),
                ('event_month', models.CharField(max_length=20)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('desc', models.TextField(max_length=500)),
                ('event_type', models.CharField(max_length=10)),
                ('event_month', models.CharField(max_length=15)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('desc', models.TextField(max_length=500)),
                ('event_type', models.CharField(max_length=10)),
                ('event_date', models.DateField()),
                ('photos', s3direct.fields.S3DirectField()),
                ('registration_url', models.URLField(blank=True, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('desc', models.TextField(max_length=500)),
                ('image', s3direct.fields.S3DirectField()),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('enrollment_number', models.CharField(blank=True, max_length=11, null=True)),
                ('image', s3direct.fields.S3DirectField()),
                ('dept', models.CharField(default='BCA', max_length=6)),
                ('core', models.BooleanField(default=False)),
                ('position', models.CharField(max_length=30)),
                ('github', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('behance', models.URLField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'members',
                'verbose_name_plural': 'Members',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, null=True)),
                ('developed', models.BooleanField(default=True)),
                ('desc', models.TextField(max_length=500, null=True)),
                ('tools', models.CharField(max_length=100)),
                ('screenshot', s3direct.fields.S3DirectField(blank=True, null=True)),
                ('source_code', models.URLField(blank=True, null=True)),
                ('live_url', models.URLField(blank=True, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ManyToManyField(blank=True, null=True, to='website.Member')),
            ],
            options={
                'db_table': 'projects',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='poc',
            field=models.ManyToManyField(blank=True, null=True, to='website.Member'),
        ),
    ]
