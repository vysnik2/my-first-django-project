# Generated by Django 4.2.7 on 2023-11-27 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import myauth.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('agreement_accepted', models.BooleanField(default=False)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=myauth.models.profile_avatar_directory_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
