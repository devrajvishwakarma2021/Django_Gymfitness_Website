# Generated by Django 4.0.6 on 2023-03-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_enrollment_duedate_enrollment_paymentstatus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='gallery')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]