# Generated by Django 4.1 on 2022-09-03 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("myblog", "0005_blogpost"),
    ]

    operations = [
        migrations.AddField(
            model_name="quillpost",
            name="authors",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="quillpost",
            name="title",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]