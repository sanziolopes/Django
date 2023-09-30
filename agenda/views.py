from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import time

from .models import Agenda

# Create your views here.
# @login_required(login_url="/signin")
def index(request):
    print('resposta',request.method)
    if request.method == "GET":
        table = Agenda.objects.all()

        a1 = 11
        a2 = 11
        a3 = 11
        a4 = 11
        a5 = 11
        a6 = 11
        a7 = 11
        a8 = 11
        a9 = 11
        a10 = 11
        a11 = 11
        a12 = 11
        a13 = 11
        a14 = 11
        a15 = 11
        a16 = 11
        a17 = 11
        a18 = 11
        a19 = 11
        a20 = 11
        a21 = 11
        a22 = 11
        a23 = 11

        for t in table:
            if t.atv1 == 'Mandala': 
                a1 -= 1
            if t.atv1 == 'Porta ATC': 
                a2 -= 1
            if t.atv2 == 'Cactus': 
                a3 -= 1
            if t.atv2 == 'Tess 1': 
                a4 -= 1
            if t.atv2 == 'Museo de Arte de Bolsillo': 
                a5 -= 1
            if t.atv3 == 'Moldura': 
                a6 -= 1
            if t.atv3 == 'Tess': 
                a7 -= 1
            if t.atv3 == 'Kusudam': 
                a8 -= 1
            if t.atv4 == 'Mandala 2': 
                a9 -= 1
            if t.atv4 == 'Broto de Papel': 
                a10 -= 1
            if t.atv4 == 'Bordado': 
                a11 -= 1
            if t.atv5 == 'RuBa III': 
                a12 -= 1
            if t.atv5 == 'Estrela Machi': 
                a13 -= 1
            if t.atv5 == 'Bordado 2': 
                a14 -= 1
            if t.atv6 == 'Flor de Froissage': 
                a15 -= 1
            if t.atv6 == 'Chinese thread book': 
                a16 -= 1
            if t.atv6 == 'Rosa': 
                a17 -= 1
            if t.atv7 == 'RuBa I': 
                a18 -= 1
            if t.atv7 == 'Porta óculos': 
                a19 -= 1
            if t.atv7 == 'Floco de neve': 
                a20 -= 1
            if t.atv8 == 'Mandala 3': 
                a21 -= 1
            if t.atv8 == 'Caixa': 
                a22 -= 1
            if t.atv8 == 'Bordado 3': 
                a23 -= 1

        context = {
            "quantity_1": a1,
            "quantity_2": a2,
            "quantity_3": a3,
            "quantity_4": a4,
            "quantity_5": a5,
            "quantity_6": a6,
            "quantity_7": a7,
            "quantity_8": a8,
            "quantity_9": a9,
            "quantity_10": a10,
            "quantity_11": a11,
            "quantity_12": a12,
            "quantity_13": a13,
            "quantity_14": a14,
            "quantity_15": a15,
            "quantity_16": a16,
            "quantity_17": a17,
            "quantity_18": a18,
            "quantity_19": a19,
            "quantity_20": a20,
            "quantity_21": a21,
            "quantity_22": a22,
            "quantity_23": a23
        }
        return render(request,'index.html',context=context)
    
    elif request.method == "POST":
    
        if request.POST.get('1') == None:
            atv1 = 'none'
        else:
            atv1 = request.POST.get('1')
        if request.POST.get('2') == None:
            atv2 = 'none'
        else:
            atv2 = request.POST.get('2')
        if request.POST.get('3') == None:
            atv3 = 'none'
        else:
            atv3 = request.POST.get('3')
        if request.POST.get('4') == None:
            atv4 = 'none'
        else:
            atv4 = request.POST.get('4')
        if request.POST.get('5') == None:
            atv5 = 'none'
        else:
            atv5 = request.POST.get('5')
        if request.POST.get('6') == None:
            atv6 = 'none'
        else:
            atv6 = request.POST.get('6')
        if request.POST.get('7') == None:
            atv7 = 'none'
        else:
            atv7 = request.POST.get('7')
        if request.POST.get('8') == None:
            atv8 = 'none'     
        else:
            atv8 = request.POST.get('8')

        try:
            register = Agenda.objects.get(user=request.POST.get('user'))
            register.delete()
        except:
            pass
        

        agenda = Agenda(
            atv1 = atv1,
            atv2 = atv2,
            atv3 = atv3,
            atv4 = atv4,
            atv5 = atv5,
            atv6 = atv6,
            atv7 = atv7,
            atv8 = atv8,
            user = request.POST.get('user')
        )

        agenda.save()
        time.sleep(1)


        resp_agenda_user = Agenda.objects.filter(user=request.POST.get('user')).last()
        
        resp = {
            "resp_agenda_user":resp_agenda_user,
            "atv1":atv1,
            "atv2":atv2,
            "atv3":atv3,
            "atv4":atv4,
            "atv5":atv5,
            "atv6":atv6,
            "atv7":atv7,
            "atv8":atv8
        }

        return render(request, 'confirmation.html',resp)

def database(request):
    print(request)

def signin(request):
    if request.method == "GET":
        return render(request,'signin.html')
    elif request.method == "POST":
        print(request)
        
        print(request.POST.get('username'))
        print(request.POST.get('password'))
        
        user = authenticate(request=request,username=request.POST.get('username'), password=request.POST.get('password') )
        print('user',user)
        if user:
            print('Autenticado')
            return render(request,'index.html',{'nome':request.POST.get('username')})
        else:
            return HttpResponse('Senha inválida')

def signup(request):
    if request.method == "GET":
        return render(request,'signup.html')
    elif request.method == "POST":
        User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password')
        )

        return render(request,'signin.html')