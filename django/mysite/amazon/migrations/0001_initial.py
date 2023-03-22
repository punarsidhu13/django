# Generated by Django 4.1.7 on 2023-03-13 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amazon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=150)),
                ('quantity', models.CharField(max_length=100)),
                ('orders', models.CharField(max_length=10)),
                ('ordered_items', models.CharField(max_length=200)),
            ],
        ),
    ]
