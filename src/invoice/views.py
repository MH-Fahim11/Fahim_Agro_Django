from django.shortcuts import render
# from .models import Coustomer
def invoice(req):
    # mymembers = Coustomer.objects.all().values()
    # context = {
    # 'mymembers': mymembers,
    # }
    return render(req,"invoice/all_invoice.html",{})