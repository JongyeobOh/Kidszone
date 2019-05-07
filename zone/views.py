from django.shortcuts import render, redirect
from .models import Board, Kidszone, Boards, Review
import pdb

# Create your views here.
def main(request):
    return render(request, 'zone/main.html')
    
    
def commu(request):
    boards = Board.objects.all()
    return render(request, 'zone/commu.html', {'boards': boards})


    
def notice(request):
    boardss = Boards.objects.all()
    return render(request, 'zone/notice.html', {'boardss': boardss})
    

def babyinfo(request):
    return render(request, 'zone/babyinfo.html')
    
def notice_board(request):
    if (request.method == "POST") and (request.POST.get('password') == "admin"):
       title = request.POST.get('title')
       description = request.POST.get('description')
       password = request.POST.get('password')
       boardss = Boards(title=title, password=password, description=description)
       boardss.save()
       return redirect('notice')
    
    return render(request, 'zone/notice_board.html')
        
    
def notice_detail(request, id):
    item = Boards.objects.get(pk=id)
    return render(request, 'zone/notice_detail.html',{'item': item})

def board(request):
    if request.method=="POST":
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
    boards = Board.objects.get(pk=id)
    if (request.method=="POST") and (boards.password == request.POST.get('password')):
        
        title = request.POST.get('title')
        nick =  request.POST.get('nick')
        description = request.POST.get('description')
        
        boards.title=title
        boards.description=description
        boards.nick=nick
        boards.save()
        return redirect('detail', boards.pk)
    return render(request, 'zone/upd.html',{'boards': boards})
    
def dele(request, id):  
    if request.method == "POST":
        Board.objects.get(pk=id).delete()
        
    return redirect('commu')

    
     
def milk(request):
    return render(request,'zone/milk.html')
    
    
def sick(request):
    return render(request, 'zone/sick.html')
    
def yet(request):
    return render(request, 'zone/yet.html')
    

def intro(request):
    kidszones = Kidszone.objects.all()
    return render(request, 'zone/intro.html', {'kidszones': kidszones})


def create(request):
    if request.method=="POST":
        title=request.POST.get('title')
        location=request.POST.get('location')
        description=request.POST.get('description')
        password=request.POST.get('password')
        image=request.FILES['image_upload']
        
        kidszone=Kidszone(title=title, location=location, description=description, image=image, password=password)
        kidszone.save()
        return redirect('intro')
    return render(request,'zone/create.html')
    
def show(request, id):
    kidszone = Kidszone.objects.get(pk=id)
    return render(request, 'zone/show.html', {'kidszone': kidszone})
    
    

def update(request,id):
    kidszone = Kidszone.objects.get(pk=id)
    if (request.method=="POST") and (kidszone.password == request.POST.get('password')):
        title = request.POST.get('title')
        location = request.POST.get('location')
        description = request.POST.get('description')
        image=request.FILES['image_upload']
        kidszone.image = image
        kidszone.title = title
        kidszone.location = location
        kidszone.description = description
        kidszone.save()
        return redirect('show', kidszone.pk)
    return render(request, 'zone/update.html', {'kidszone': kidszone})

    
def delete(request,id):
    kidszone = Kidszone.objects.get(pk=id)
    if (request.method=="POST") and (kidszone.password == request.POST.get('password')):
    	kidszone=Kidszone.objects.get(pk=id)
    	kidszone.delete()
    	return redirect('intro')
    return render(request, 'zone/show.html', {'kidszone': kidszone})
    
def delee(request, id):  
    if request.method == "POST":
        pw = request.POST.get('password')
        if pw == "admin":
           
            b=Boards.objects.get(pk=id)
            b.delete()
        
        return redirect('notice')
    return redirect('notice')
    
    
    

def mapp(request):
    return render(request, 'zone/mapp.html')    
    
    
def co_create(request, id):
    if request.method=="POST":
        title=request.POST.get('title')
        writer=request.POST.get('writer')
        your_review=request.POST.get('your_review')
        password=request.POST.get('password')
        try:
            image=request.FILES['image']
        except:
            image = "../static/image/baby.png"
        review=Review(title=title, writer=writer, your_review=your_review, image=image, password=password, kidszoneID=id)
        review.save()
        return redirect('comment', id)
    kidszoneid = id
    return render(request,'zone/co_create.html', {'kidszoneid':kidszoneid})

    
def comment(request,id):
    reviews = Review.objects.filter(kidszoneID = id)
    kidszoneid = id
    return render(request,'zone/comment.html',{ 'reviews': reviews, 'kidszoneid': kidszoneid })
    

def co_show(request, id):
    reviews = Review.objects.get(id = id)
    kidszoneid = id
    
    return render(request, 'zone/co_show.html', {'reviews': reviews, 'kidszoneid': kidszoneid})
    
    
def co_update(request,id):
    review = Review.objects.get(id = id)
    if (request.method=="POST") and (review.password == request.POST.get('password')):
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        your_review = request.POST.get('your_review')
        image=request.FILES['image']
        review.image = image
        review.title = title
        review.writer = writer
        review.your_review = your_review
        review.save()
        return redirect('co_show', review.id)
    return render(request, 'zone/co_update.html', {'review': review })
    
    
def co_delete(request, id):
    review = Review.objects.get(id = id)
    if (request.method=="POST") and (review.password == request.POST.get('password')):
    	review=Review.objects.get(id = id)
    	review.delete()
    	return redirect('comment', review.kidszoneID)
    return render(request, 'zone/co_show.html', {'review': review})