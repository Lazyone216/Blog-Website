# Generated by Django 4.2.6 on 2023-11-12 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comments_options_posts_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
