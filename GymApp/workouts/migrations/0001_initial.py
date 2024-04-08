# Generated by Django 4.2.10 on 2024-04-08 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_type', models.CharField(choices=[('gym', 'Gym'), ('cross_fit', 'Cross Fit'), ('gym_and_cross_fit', 'Gym + Cross Fit'), ('pt', 'Personal Training')], max_length=40)),
                ('amount', models.CharField(max_length=10)),
                ('duration', models.CharField(max_length=10)),
                ('photo', models.FileField(blank=True, upload_to='photos/')),
                ('gym_workouts', models.CharField(blank=True, max_length=100, null=True)),
                ('cross_fit_details', models.TextField(blank=True, null=True)),
                ('personal_training_details', models.CharField(blank=True, max_length=100, null=True)),
                ('personal_training_hours', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
