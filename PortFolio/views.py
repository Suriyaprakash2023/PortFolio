from django.shortcuts import render, redirect

def index(request):
  return render(request,'projects.html') #Index.html have the orginal code