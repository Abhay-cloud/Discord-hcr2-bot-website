# Generated by Django 3.1 on 2020-10-13 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('helpContent', models.TextField()),
                ('permissions', models.CharField(max_length=255)),
            ],
        ),
    ]
