# Generated by Django 2.1.4 on 2019-03-13 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0009_account_bindinguser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='money',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
