# Generated by Django 2.0.4 on 2019-04-26 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]