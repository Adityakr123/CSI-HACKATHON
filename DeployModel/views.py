from pickle import GET
from django.http import HttpResponse
from django.shortcuts import render
import joblib
def home(request):
    return render(request,"home.html")
def result(request):
    cls = joblib.load('finalized_model.sav')
    lis=[]
    a=request.GET['a']
    if a=="M":
        a=1
    elif a=="F":
        a=0
    lis.append(a)
    i=request.GET['i']
    lis.append(i)
    b=request.GET['b']
    if b=="Y":
        b=1
    elif b=="N":
        b=0
    lis.append(b)
    c=request.GET['c']
    if c=="Y":
        c=1
    elif c=="N":
        c=0
    lis.append(c)

    d=request.GET['d']
    if d=="Y":
        d=1
    elif d=="N":
        d=0
    lis.append(d)
    e=request.GET['e']
    if e=="G":
        e=1
    elif e=="P":           
        e=0.5
    elif e=="S":
        e=0
    elif e=="N":
        e=2
    
    lis.append(e)
    j=request.GET['j']
    if j=="O":
        j=1
    elif j=="R":           
        j=0
    lis.append(j)
    lis.append(request.GET['f'])
    lis.append(request.GET['g'])
    h=request.GET['h']
    if h=="R":
        h=1
    elif h=="F":
        h=0.5
    elif h=="N":
        h=0
    lis.append(h)
   
    # print(lis)
    ans=cls.predict([lis])

    
    if ans==1:
        ans="YOU HAVE HIGH CHANCE OF  HAVING STROKE"
        an="Lower Your Blood Pressure. \nStay Away From Smoking.\n Manage Your Heart.\n Cut the Booze.\n Control Your Diabetes.Exercise.\n Eat Better Foods.\n Watch the Cholesterol."
        
    else:
        ans="YOU  HAVE MINIMAL CHANCES TO HAVE STROKE"
        an=" "
         
    return render(request,"result.html",{'ans':ans,'an':an})
def stroke(request):
    return render(request,"stroke.html")
def heart(request):
    
    return render(request,"heart.html")
def sugar(request):
    
    return render(request,"sugar.html")
def sresult(request):
    cls2 = joblib.load('sfinalized_model.sav')
    list1=[]

    list1.append(float(request.GET['a2']))
    list1.append(float(request.GET['b2']))
    list1.append(float(request.GET['c2']))
    list1.append(float(request.GET['d2']))
    list1.append(float(request.GET['e2']))
    list1.append(float(request.GET['f2']))
    list1.append(float(request.GET['g2']))
    list1.append(float(request.GET['h2']))
    ans2=cls2.predict([list1])
    if ans2==1:
        ans2="You are prone to diabetes"
    else:
         ans2="You are not prone to diabetes"


    return render(request,"sresult.html",{'ans2':ans2})


    
def hresult(request):
    cls1 = joblib.load('hfinalized_model.sav')
    list=[]
    list.append(request.GET['a1'])
    
    b1=request.GET['b1']
    if b1=="M":
        b1=1
    elif b1=="F":
        b1=0
    list.append(b1)
    list.append(request.GET['c1'])
    list.append(request.GET['d1'])
    list.append(request.GET['e1'])
    f1=request.GET['f1']
    if f1=="H":
        f1=1
    else:
        f1=0
    list.append(f1)
    g1=request.GET['g1']
    if g1=="H":
        g1=1
    else:
        g1=0
    list.append(g1)
    list.append(request.GET['h1'])
    i1=request.GET['i1']
    if i1=="H":
        i1=1
    else:
        i1=0
    list.append(i1)
    list.append(request.GET['j1'])
    list.append(request.GET['k1'])
    list.append(request.GET['l1'])
    list.append(request.GET['m1'])
    ans1=cls1.predict([list])
    if ans1==1:
        ans1="You are prone to Heart Attack"

    else:
         ans1="You are not prone to Heart Attack"


    return render(request,"hresult.html",{'ans1':ans1})
