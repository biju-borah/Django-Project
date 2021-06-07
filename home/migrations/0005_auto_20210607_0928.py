# Generated by Django 3.2.1 on 2021-06-07 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_message_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='img',
        ),
        migrations.RemoveField(
            model_name='project',
            name='price',
        ),
        migrations.AddField(
            model_name='project',
            name='language',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='month',
            field=models.TextField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
