from django.db import models

# Create your models here.
class Admin(models.Model):
    AdName=models.CharField(max_length=20)
    AdEmail=models.CharField(max_length=20,unique=True)
    AdPass=models.CharField(max_length=20)

class User(models.Model):
    UName=models.CharField(max_length=20)
    UEmail=models.CharField(max_length=20,unique=True)
    UPass=models.CharField(max_length=20)
    UDOB=models.CharField(max_length=20)

class Quiz(models.Model):
    QuizName=models.CharField(max_length=20)
    QuizID=models.IntegerField()
    Ques=models.CharField(max_length=40,null=False,blank=False)
    Op1=models.CharField(max_length=20)
    Op2=models.CharField(max_length=20)
    Op3=models.CharField(max_length=20)
    Op4=models.CharField(max_length=20)
    Ans=models.CharField(max_length=20)
    def __str__(self):
        return self.QuizName+" "+self.Ques+" "+self.Op1+" "+self.Op2+" "+self.Op3+" "+self.Op4+" "+self.Ans

class AllQuiz(models.Model):
    QuizID=models.IntegerField(unique=True)
    QuizName=models.CharField(max_length=20)
    def __str__(self):
        return str(self.QuizID)+" "+str(self.QuizName)



