from django.shortcuts import render

def home_view(req):
    return render(req,"pages/home.html",{})