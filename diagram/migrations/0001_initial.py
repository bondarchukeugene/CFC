# Generated by Django 3.2.2 on 2021-05-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Possesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mother', models.CharField(max_length=20)),
                ('child', models.CharField(max_length=20)),
            ],
        ),
    ]