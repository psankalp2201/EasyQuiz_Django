# Generated by Django 4.0.6 on 2022-08-31 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyQuiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='Ans',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]