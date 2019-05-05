from django.shortcuts import render, redirect
from .models import Board, Kidszone


# Create your views here.
def main(request):
    return render(request, 'zone/main.html')
    
    
def commu(request):
    boards = Board.objects.all()
    return render(request, 'zone/commu.html', {'boards': boards})


def babyinfo(request):
    return render(request, 'zone/babyinfo.html')
    
    
def introo(request):
    return render(request, 'zone/introo.html')
    
    
def Q_A(request):
    return render(request, 'zone/Q_A.html')
    
    
def notice(request):
    return render(request, 'zone/notice.html')
    

def board(request):
    if request.method == "POST":
       title = request.POST.get('title')
       description = request.POST.get('description')
       boards = Board(title=title, description=description)
       boards.save()
       return redirect('commu')
    
    return render(request, 'zone/board.html')
    
    
def milk(request):
    return render(request,'zone/milk.html')
    
    
def sick(request):
    return render(request, 'zone/sick.html')
    

def intro(request):
    kidszones = Kidszone.objects.all()
    print(kidszones)
    return render(request, 'zone/intro.html', {'kidszones': kidszones})


def create(request):
    kidszone = Kidszone.objects.create()
    if request.method=="POST":
        title=request.POST.get('title')
        location=request.POST.get('location')
        description=request.POST.get('description')
        kidszone=Kidszone(title=title, location=location, description=description)
        kidszone.save()
        return redirect('intro')
    return render(request,'zone/create.html')