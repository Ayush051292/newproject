# Generated by Django 4.2.3 on 2023-08-03 09:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_emp_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='text_body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='file',
            field=models.FileField(null=True, upload_to='emp_file'),
        ),
    ]
