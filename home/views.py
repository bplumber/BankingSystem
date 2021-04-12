from django.shortcuts import render, redirect
from .models import Customers, Transactions
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "home.html")

def cust(request):
    custs = Customers.objects.all()
    return render(request, 'cust.html', {'custs':  custs})

def trans(request):
    trans = Transactions.objects.all()
    return render(request, 'trans.html', {'trans':trans})  

def transaction(request):
    sacc_num = int(request.POST['sacc_num'])
    racc_num = int(request.POST['racc_num'])
    amount = int(request.POST.get('amount'))
    sender = Customers.objects.get(acc_num=sacc_num) 
    reciever = Customers.objects.get(acc_num=racc_num)
    sname = sender.name
    rname = reciever.name
    samt = sender.amt
    ramt = reciever.amt
    if samt < amount:
        messages.info(request, 'Insuffient Balance')
        return redirect('cust')
    else:
        samt = samt - amount
        ramt = ramt + amount
        Customers.objects.filter(acc_num=sacc_num).update(amt=samt)
        Customers.objects.filter(acc_num=racc_num).update(amt=ramt)
        custs = Customers.objects.all()
        b2 = Transactions(sacc_num=sacc_num, racc_num=racc_num, sname = sname, rname = rname, amt = amount)
        b2.save()
        return render(request, 'cust.html', {'custs':custs})