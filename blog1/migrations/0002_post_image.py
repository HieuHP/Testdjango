# Generated by Django 2.0.3 on 2020-05-06 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]