# Generated by Django 4.2.5 on 2023-11-01 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0002_alter_post_options_post_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="date",
            field=models.CharField(default=200, max_length=200),
            preserve_default=False,
        ),
    ]