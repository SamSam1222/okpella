# Generated by Django 4.2.4 on 2023-12-08 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpMembers', '0012_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='discipline',
            field=models.CharField(max_length=90),
        ),
    ]
