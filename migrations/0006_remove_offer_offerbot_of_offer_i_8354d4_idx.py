# Generated by Django 4.2 on 2023-04-29 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_offer_offerbot_of_offer_i_8354d4_idx_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='offer',
            name='offerbot_of_offer_i_8354d4_idx',
        ),
    ]
