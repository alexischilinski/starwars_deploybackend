# Generated by Django 3.0.2 on 2020-02-03 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('climate', models.CharField(max_length=200)),
                ('terrain', models.CharField(max_length=200)),
            ],
        ),
    ]