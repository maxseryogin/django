# Generated by Django 5.1 on 2024-09-02 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(choices=[('admin', 'admin'), ('user', 'user')], default='user', max_length=5)),
            ],
        ),
    ]
