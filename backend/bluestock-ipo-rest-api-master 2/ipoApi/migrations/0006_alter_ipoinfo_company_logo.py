# Generated by Django 5.0.7 on 2024-08-08 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipoApi', '0005_ipoinfo_company_logo_ipoinfo_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipoinfo',
            name='company_logo',
            field=models.ImageField(blank=True, null=True, upload_to='company_images/'),
        ),
    ]
