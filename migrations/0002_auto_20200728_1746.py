# Generated by Django 3.0.8 on 2020-07-28 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=250, verbose_name='заголовок статьи'),
        ),
    ]