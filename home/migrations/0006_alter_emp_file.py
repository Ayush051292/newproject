# Generated by Django 4.2.3 on 2023-08-01 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_emp_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='file',
            field=models.FileField(null=True, upload_to='home/uploads'),
        ),
    ]
