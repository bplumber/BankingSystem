# Generated by Django 3.1.7 on 2021-04-08 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_num', models.IntegerField()),
                ('ifsc', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('amt', models.IntegerField()),
            ],
        ),
    ]
