# Generated by Django 4.0.3 on 2022-04-29 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_alter_profile_pix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pix',
            field=models.ImageField(blank=True, default='profile/avatar.png', null=True, upload_to='profile'),
        ),
    ]
