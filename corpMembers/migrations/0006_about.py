# Generated by Django 4.2.4 on 2023-09-07 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpMembers', '0005_contact_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='about_images/')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
    ]
