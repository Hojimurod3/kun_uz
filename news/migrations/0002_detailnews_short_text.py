# Generated by Django 5.0.1 on 2024-01-17 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailnews',
            name='short_text',
            field=models.CharField(default=1234, max_length=255),
            preserve_default=False,
        ),
    ]