# Generated by Django 4.2.4 on 2023-10-01 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpMembers', '0010_delete_cdsgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
