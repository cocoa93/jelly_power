from django.shortcuts import render

def mypage(request):
    return render(request,"mypage.html",{})

def wish_list(request):
    return render(request,"wish_list.html",{})

def cart(request):
    return render(request,"cart.html",{})