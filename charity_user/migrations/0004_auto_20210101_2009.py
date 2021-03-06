# Generated by Django 3.1.4 on 2021-01-01 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter_topic', '0002_auto_20201228_1822'),
        ('charity_user', '0003_auto_20201228_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charityuser',
            name='subscribed_newsletter_topics',
            field=models.ManyToManyField(blank=True, related_name='subscribed_users', to='newsletter_topic.NewsletterTopic'),
        ),
    ]
