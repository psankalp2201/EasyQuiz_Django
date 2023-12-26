
from logging import exception
from django.db import IntegrityError
from django.db.models import Max
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from EasyQuiz.models import *

# Create your views here.

i=-1
crct=-1

def home(request1):
    return render(request1,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def quiz(request):
    return render(request,'quiz.html')

def signup_admin(request):
    return render(request,'signup_admin.html')

def signup_user(request):
    return render(request,'signup_user.html')

def login_admin(request):
    return render(request,'login_admin.html')

def login_user(request):
    return render(request,'login_user.html')

def profile_admin(request):
    if 'admin_type' in request.session.keys():
        return render(request,'profile_admin.html')
    return redirect('/EasyQuiz/quiz')

def quiz(request):
    return render(request,'quiz.html')

def sample(request):
    return render(request,'sample.html')

def create_quiz(request):
    if 'admin_type' in request.session.keys():
        return render(request,'create_quiz.html',{'qn':"5",'qid':"01"})
    return redirect('/EasyQuiz/quiz')
    

def update_quiz(request):
    return render(request,'update_quiz.html')

def view_all_quiz(request):
    if 'admin_type' in request.session.keys():
        obj=AllQuiz.objects.all()
        mx=AllQuiz.objects.count()
        return render(request,'view_all_quiz.html',{'obj':obj})
    return redirect('/EasyQuiz/quiz')

    



def profile_user(request):
    if 'user_type' in request.session.keys():
        return render(request,'profile_user.html')
    return redirect('/EasyQuiz/quiz')
    

def start_quiz(request):
    if 'user_type' in request.session.keys():
        return render(request,'start_quiz.html')
    return redirect('/EasyQuiz/quiz')
    

## Render Views Above
## Logical Views Below


def signupAdmin(request):
    if request.method=='POST':
        try:
            aname=request.POST['name']
            aemail=request.POST['email']
            apass=request.POST['password']
    
            f1=Admin(AdName=aname,AdEmail=aemail,AdPass=apass)
            f1.save()
            return render(request,'login_admin.html',{'msg':"Account Created,Please login to continue..."})
            
        except IntegrityError:
            return render(request,'signup_admin.html',{'err':"Your Email ID is already in use..."})

def loginAdmin(request):
    if request.method=='POST':
        try:
            aemail=request.POST['email']
            apass=request.POST['password']

            P=Admin.objects.get(AdEmail=aemail,AdPass=apass)
            request.session['admin_type']=aemail
            return render(request,'profile_admin.html')

        except Exception as e:
            return render(request,'login_admin.html',{'err':"Invalid Credentials"})

def signupUser(request):
    if request.method=='POST':
        try:
            uname=request.POST['name']
            uemail=request.POST['email']
            upass=request.POST['password']
            udob=request.POST['dob']
    
            f1=User(UName=uname,UEmail=uemail,UPass=upass,UDOB=udob)
            f1.save()
            return render(request,'login_user.html',{'msg':"Account Created,Please login to continue..."})
            
        except IntegrityError:
            return render(request,'signup_user.html',{'err':"Your Email ID is already in use..."})


def loginUser(request):
    if request.method=='POST':
        try:
            uemail=request.POST['email']
            upass=request.POST['password']

            P=User.objects.get(UEmail=uemail,UPass=upass)
            global i,crct
            i=-1
            crct=-1
            request.session['user_type']=uemail
            return render(request,'profile_user.html')
        except Exception:
            return render(request,'login_user.html',{'err':"Invalid Credentials"})


def createQuiz(request):
    if request.method=='POST':
        try:
            qname=request.POST['qname']
            qid=request.POST['qid']

            f1=AllQuiz(QuizName=qname,QuizID=qid)
            f1.save()
            return render(request,'create_quiz.html',{'qid':qid,'qname':qname})
        except IntegrityError:
            return render(request,'profile_admin.html',{'err':"Quiz ID already Exists"})

def addQues(request):
    if request.method=='POST':
        try:
            qid=request.POST['qid']
            qname=request.POST['qname']
            ques=request.POST['ques']
            op1=request.POST['o1']
            op2=request.POST['o2']
            op3=request.POST['o3']
            op4=request.POST['o4']
            ans=request.POST['ans']

            f1=Quiz(QuizID=qid,QuizName=qname,Ques=ques,Op1=op1,Op2=op2,Op3=op3,Op4=op4,Ans=ans)
            f1.save()
            return render(request,'create_quiz.html',{'qid':qid,'qname':qname,'msg':"Question Added Succesfully"})
        except Exception as e:
            return render(request,'create_quiz.html',{'qid':qid,'qname':qname,'err':"Fill all the blocks and try again"})

def logout_U(request):
    if 'user_type' in request.session.keys():
        del request.session["user_type"]
        return render(request,'quiz.html')

def logout_A(request):
    if 'admin_type' in request.session.keys():
        del request.session["admin_type"]
        return render(request,'quiz.html')
        
def submitQuiz(request):
    if request.method=='POST':
        try:
            qid=request.POST['qid']
            ques=request.POST['ques']

            P=User.objects.get(UEmail=qid,UPass=ques)
            return redirect('/EasyQuiz/profile')
        except:
            pass

def updateQuiz(request):
    pass


def deleteQuiz(request):
    if request.method=='POST':
        
        try:
            qid=request.POST['qid']
            P=AllQuiz.objects.get(QuizID=qid)
            Quiz.objects.filter(QuizID=qid).delete()
            AllQuiz.objects.filter(QuizID=qid).delete()

            return render(request,'profile_admin.html',{'msg':"Deletion Successful"})
        except Exception as e:
            return render(request,'profile_admin.html',{'err':"Invalid Quiz ID"})

def viewAllQuiz(request):
    pass



def viewQues(request):
    global i,crct
    ss=request.POST['qid']
    tques=Quiz.objects.filter(QuizID=ss).count()

    obj=Quiz.objects.filter(QuizID=ss)
    rans=request.POST['rans']
    ans=request.POST['op']

    if rans==ans:
        crct+=1

    if i<len(obj)-1:
            i+=1
            return render(request,'SolveQuiz.html',{'obj':obj[i],'qnum':i+1,'qid':ss,'tques':tques,'crct':crct})
    else:
        i=-1
        temp=crct
        crct=-1
        return render(request,'report.html',{'qid':ss,'score':temp,'total':tques})
        

def start_qid(request):
    
    if request.method=='POST':
        try:
            qid=request.POST['qid']
            obj=AllQuiz.objects.get(QuizID=qid)
            qname=obj.QuizName
            return render(request,'start_quiz.html',{'qid':qid,'qname':qname})
        except Exception as e:
            return render(request,'profile_user.html',{'msg':"Invalid Quiz ID"})



