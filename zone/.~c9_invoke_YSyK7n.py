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
    
    
def Q_A(request):
    return render(request, 'zone/Q_A.html')
    
    
def notice(request):
    return render(request, 'zone/notice.html')
    

def board(request):
    if request.method == "POST":
       title = request.POST.get('title')
       nick =  request.POST.get('nick')
       description = request.POST.get('description')
       password = request.POST.get('password')
       boards = Board(title=title, nick=nick, password=password, description=description)
       boards.save()
       return redirect('commu')
    
    return render(request, 'zone/board.html')
    
def detail(request, id):
    item = Board.objects.get(pk=id)
    return render(request, 'zone/detail.html',{'item': item})



def upd(request, id):
     if request.method == "POST":
       title = request.POST.get('title')
       nick =  request.POST.get('nick')
       description = request.POST.get('description')
       password = request.POST.get('password')
       boards = Board(title=title, nick=nick, password=password, description=description)
       boards.save()
       return redirect('commu', board.pk)
     return render(request, 'zone/upd.html',{'boards': boards})
    
def dele(request, id):  
    if request.method == "POST":
        Boards.objects.get(pk=id).delete()
        
    return redirect('commu')

    
     
def milk(request):
    return render(request,'zone/milk.html')
    
    
def sick(request):
    return render(request, 'zone/sick.html')
    
def yet(request):
    return render(request, 'zone/yet.html')
    

def intro(request):
        return redirect('sho,{'kidszone': kidszone})
    return render(request, 'zone/intro.html', {'kidszones': kidszones})


def create(request):
    kidszone = Kidszone.objects.create()
    if request.method=="POST":
    #  and request.FILES['upload']:
        title=request.POST.get('title')
        location=request.POST.get('location')
        description=request.POST.get('description')
        # print(request.FILES.get('upload'))
        # for filename, file in request.FILES.iteritems():
        # request.FILES[]
            # print(request.FILES[filename].name)
        print("@@",request)
        image=request.FILES['image_upload']
        # fs = FileSystemStorage()
        # imagename = fs.save(image.name, image)
        # uploaded_file_url = fs.url(imagename)
        kidszone=Kidszone(title=title, location=location, description=description, image=image)
        # kidszone.save()
        return redirect('intro')
    return render(request,'zone/create.html')
    
def show(request, id):
    kidszone = Kidszone.objects.get(pk=id)
    return render(request, 'zone/show.html', {'kidszone': kidszone})
    
    

def update(request,id):
    kidszone = Kidszone.objects.get(pk=id)
    if request.method=="POST":
        title = request.POST.get('title')
        location = request.POST.get('location')
        description = request.POST.get('description')
        kidszone.title = title
        kidszone.location = location
        kidszone.description = description
        kidszone.save()
        return redirect('show', kidszone.pk)
    return render(request, 'zone/update.html', {'kidszone': kidszone})
    
def delete(request,id):
    if request.method=="POST":
    	kidszone=Kidszone.objects.get(pk=id)
    	kidszone.delete()
    	return redirect('intro')
