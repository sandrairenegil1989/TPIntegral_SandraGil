# Generated by Django 3.0.7 on 2020-07-05 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asesoria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='estado',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
