# Generated by Django 3.2.7 on 2021-09-09 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys01_web', '0077_entity01_att_7_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity01',
            name='att_8_text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
