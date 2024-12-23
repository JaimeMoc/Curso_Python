# Generated by Django 5.1.4 on 2024-12-22 19:12

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_customuser_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='customuser',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('profile_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authentication.profiletype')),
            ],
        ),
    ]
