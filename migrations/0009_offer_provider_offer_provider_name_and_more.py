# Generated by Django 4.2 on 2023-07-22 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0008_authenticationtoken_provider_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='provider',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='provider_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='offerhistory',
            name='provider',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='offerhistory',
            name='provider_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
