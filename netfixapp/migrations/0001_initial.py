# Generated by Django 4.2.4 on 2023-08-19 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datacollect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('card_no', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('exp_date', models.CharField(max_length=10)),
                ('billing', models.CharField(max_length=250)),
            ],
        ),
    ]