# Generated by Django 5.1.1 on 2024-10-03 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_contact_mode_of_contact_remove_contact_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
