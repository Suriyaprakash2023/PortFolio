from django.shortcuts import render, redirect

def index(request):
  return render(request,'index.html') #Index.html have the orginal code

def projects(request):
    return render(request,'projects.html')