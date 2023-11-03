# Generated by Django 4.2.5 on 2023-11-03 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0004_post_img"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="booking",
            field=models.CharField(
                choices=[("yes", "館藏中"), ("no", "外借中")], default="yes", max_length=3
            ),
        ),
    ]