# Generated by Django 4.2.10 on 2024-04-08 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='trainer', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_trainer', models.BooleanField(default=True)),
            ],
        ),
    ]
