# Generated by Django 2.0.13 on 2019-06-19 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talleres', '0002_auto_20190619_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propuestas',
            name='IdPropuestas',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
