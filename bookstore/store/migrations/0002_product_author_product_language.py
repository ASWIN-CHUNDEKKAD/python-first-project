# Generated by Django 4.2.4 on 2023-08-11 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='language',
            field=models.CharField(default='exit', max_length=50),
            preserve_default=False,
        ),
    ]