# Generated by Django 2.0.1 on 2019-01-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic_description',
            field=models.CharField(default='Some string describing the topic', max_length=526),
        ),
    ]
