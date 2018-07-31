from django.shortcuts import render

# Create your views here.

def shop_main(request):
    return render(request,"shop_main.html",{})

def shop_support(request):
    return render(request,"shop_support.html",{})

def shop_goods(request):
    return render(request,"shop_goods.html",{})

def shop_support_details(request):
    return render(request,"shop_support_details.html",{})

def shop_goods_details(request):
    return render(request,"shop_goods_details.html",{})




