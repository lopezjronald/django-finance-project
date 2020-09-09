# Generated by Django 3.1.1 on 2020-09-08 11:53

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phone_field.models.PhoneField(help_text='Phone Contact', max_length=31)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('cover_letter', models.FileField(blank=True, upload_to='covers/')),
                ('additional_information', models.TextField()),
            ],
        ),
    ]