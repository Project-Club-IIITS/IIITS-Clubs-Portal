# Generated by Django 2.1.3 on 2019-01-21 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='full_name',
            field=models.CharField(default='Project Club IIITS', max_length=100),
            preserve_default=False,
        ),
    ]