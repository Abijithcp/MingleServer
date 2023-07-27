# Generated by Django 4.2 on 2023-05-18 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_user_default_cover_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='default_cover_image',
        ),
        migrations.AddField(
            model_name='user',
            name='cover_picture',
            field=models.ImageField(default='userCover/default_cover.png', upload_to='userCover/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='userImage/default_profilePic.png', upload_to='userImage/'),
        ),
    ]