# Generated by Django 4.0.6 on 2022-09-02 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EasyQuiz', '0003_alter_admin_ademail_alter_user_uemail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='Ans',
            new_name='QuizName',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='Op1',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='Op2',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='Op3',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='Op4',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='Ques',
        ),
    ]
