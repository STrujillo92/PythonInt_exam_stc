# Generated by Django 5.1.3 on 2024-12-01 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platillo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='platillo',
            name='procedencia',
            field=models.CharField(default='exit', max_length=60),
            preserve_default=False,
        ),
    ]
