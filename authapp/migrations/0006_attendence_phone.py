# Generated by Django 4.0.6 on 2023-03-20 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_attendence'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='phone',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]
