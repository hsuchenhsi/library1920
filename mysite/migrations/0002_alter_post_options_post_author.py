# Generated by Django 4.2.5 on 2023-11-01 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(name="post", options={"ordering": ("pub_date",)},),
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.CharField(default=200, max_length=200),
            preserve_default=False,
        ),
    ]