# Generated by Django 4.2.5 on 2023-10-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_tag_note_tag_alter_note_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]