# Generated by Django 2.2.4 on 2019-08-08 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nomePerson', models.CharField(max_length=100)),
                ('idade', models.IntegerField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Pessoas',
                'db_table': 'Pessoas',
                'ordering': ['nomePerson'],
            },
        ),
    ]
