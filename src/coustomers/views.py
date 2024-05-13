from django.shortcuts import render
from .models import Coustomer
def coustomers(req):
    mymembers = Coustomer.objects.all().values()
    context = {
    'mymembers': mymembers,
    }
    return render(req,"coustomers/coustomers.html",context)