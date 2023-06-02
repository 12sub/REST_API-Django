# Generated by Django 4.2.1 on 2023-05-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('democode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('information', models.CharField(max_length=150)),
                ('description', models.TextField(default=None)),
                ('date_of_birth', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
