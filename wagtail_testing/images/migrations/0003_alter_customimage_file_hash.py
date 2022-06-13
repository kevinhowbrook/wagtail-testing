# Generated by Django 4.0.5 on 2022-06-13 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0002_customimage_file_hash"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customimage",
            name="file_hash",
            field=models.CharField(
                blank=True, db_index=True, editable=False, max_length=40
            ),
        ),
    ]