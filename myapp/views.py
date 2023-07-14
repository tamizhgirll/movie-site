from django.shortcuts import render, redirect, get_object_or_404
from myapp.forms import MovieForm, SignupForm
from myapp.models import Movies
from django.template.defaulttags import register
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def homePage(request):
    movies = Movies.objects.all()
    return render(request,'home.html',{'movies':movies})

@register.filter
def get_range(value):
    return range(value)

@login_required()
def profile(request):
    return render(request,'profile.html')

def detailView(request,id):
    data = get_object_or_404(Movies,pk=id)
    return render(request,'details.html',{'details':data})

@login_required()
def addMovie(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request,'add.html',{'form':form})

@login_required()
def viewMovies(request):
    movies = Movies.objects.all()
    return render(request,'view.html',{'mov':movies})

@login_required()
def editMovie(request,id):
    data = get_object_or_404(Movies,pk=id)
    form = MovieForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return redirect('view')
    return render(request,'edit.html',{"form":form})

@login_required()
def deleteMovie(request,id):
    data = get_object_or_404(Movies, pk=id)
    if request.method=="POST":
        data.delete()
        return redirect('view')
    return render(request, 'delete.html', {"data": data})

def signupPage(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse('Account Created Successfully!')
    return render(request,'signup.html',{'form':form})