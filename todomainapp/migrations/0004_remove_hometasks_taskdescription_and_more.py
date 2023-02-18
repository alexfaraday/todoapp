# Generated by Django 4.1.6 on 2023-02-18 17:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todomainapp', '0003_alter_hometasks_taskcreatedate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hometasks',
            name='taskdescription',
        ),
        migrations.RemoveField(
            model_name='hometasks',
            name='taskstartdate',
        ),
        migrations.AlterField(
            model_name='hometasks',
            name='taskcreatedate',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='hometasks',
            name='taskenddate',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]