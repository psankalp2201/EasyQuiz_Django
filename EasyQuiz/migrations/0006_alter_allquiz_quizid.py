# Generated by Django 4.0.6 on 2022-09-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyQuiz', '0005_allquiz_quiz_ans_quiz_op1_quiz_op2_quiz_op3_quiz_op4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allquiz',
            name='QuizID',
            field=models.IntegerField(unique=True),
        ),
    ]
