# Generated by Django 4.0.4 on 2022-06-22 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_alter_tinymodel_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='tinymodel',
            name='short_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tinymodel',
            name='hash',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]