from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class AdditionView(View):
    def get(self,request,*args,**kwargs):
        return render (request,'add.html')
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)+int(n2)
        print("result=",result)
        return render(request,"Add.html",{"data":result})
    
class SubstractionView(View):
    def get(self,request,*args,**kwargs):
        return render (request,'sub.html')
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)-int(n2)
        print("result=",result)
        return render(request,"sub.html",{"data":result})
    
class MultiplicatioView(View):
    def get (self,request,*args,**kwargs):
        return render (request,'mul.html')
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)*int(n2)
        print("result=",result)
        return render(request,"mul.html",{"data":result})

class leapYearView(View):

    def get(self,request,*args,**kwargs):
        return render(request,'year.html')
    
    def post(self,request,*args,**kwargs):
        year=int(request.POST.get("year"))
        res="" 
        if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
            res="Is Leap Year"
        else:
             res="Not Leap Year"
        return render(request,"year.html",{"data":res})
    
class EMIView(View):

    def get(self,request,*args,**kwargs):
        return render(request,'emi.html')
    
    def post(self,request,*args,**kwargs):
        loan_amount=int(request.POST.get("amount"))
        intrest_rate=int(request.POST.get("interest"))
        tenure=int(request.POST.get("tenure"))
        p=loan_amount
        r=intrest_rate/12
        i=r/100
        n=tenure*12
        one_plus_power=(1+i)**n
        EMI=round((p*i*one_plus_power)/(one_plus_power-1))
        print(f"emi amount={EMI}")
        total_interest_payable=(EMI*n)-p 
        total_payment=total_interest_payable+p
        context={
            "emi":EMI,
            "tip":total_interest_payable,
            'tp':total_payment
        }

        return render(request,'emi.html',context)
    
class IndexView(View):
    
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")
    
from django import forms

# form class 
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField
    

# view class 
class SigninView(View):
    def get(self,request,args,*kwargs):

        form=LoginForm()   # copy of login form, an obj
        return render(request,"login.html",{"form":form})
    


# registration
# fname
# lname
# email
# username
# password

class RegistartionForm(forms.Form):
    first_name=forms.CharField(label="firstName")
    last_name=forms.CharField(label="LastName")
    email=forms.EmailField(label="email")
    username=forms.CharField(label="userName")
    password=forms.CharField(label="Password")


class SignupView(View):
    def get(self,request,*args,**kwargs):
        form=RegistartionForm()
        return render(request,"signup.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistartionForm()
        print(request.POST.get("first_name"))
        print(request.POST.get("last_name"))
        print(request.POST.get("email"))
        print(request.POST.get("username"))
        print(request.POST.get("password"))

        return render (request,"signup.html",{"form":form})