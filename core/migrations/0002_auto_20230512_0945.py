# Generated by Django 3.1.2 on 2023-05-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='vencimiento',
        ),
        migrations.AddField(
            model_name='tipoproducto',
            name='nombre',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]