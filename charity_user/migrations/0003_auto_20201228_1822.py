# Generated by Django 3.1.4 on 2020-12-28 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("charity_user", "0002_charityuser_subscribed_newsletter_topics"),
    ]

    operations = [
        migrations.AlterField(
            model_name="charityuser",
            name="phone_number",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
