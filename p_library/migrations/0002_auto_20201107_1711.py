# Generated by Django 3.1.2 on 2020-11-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redaction',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
