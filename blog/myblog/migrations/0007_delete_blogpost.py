# Generated by Django 4.1 on 2022-09-03 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myblog", "0006_quillpost_authors_quillpost_title"),
    ]

    operations = [
        migrations.DeleteModel(name="blogPost",),
    ]