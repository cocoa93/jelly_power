from django.shortcuts import render


def index(request):
    return render(request,"staticpages/index.html",{})

def about(request):
    return render(request,"staticpages/about.html",{})

def join(request):
    return render(request,"staticpages/join.html",{})

def welcome(request):
    return render(request,"staticpages/welcome.html",{})
