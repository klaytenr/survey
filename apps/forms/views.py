from __future__ import unicode_literals
from django.shortcuts import render, redirect 

# Create your views here.

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request, 'forms/index.html')

def process(request):
    if request.method == "POST":
        request.session['count'] += 1
        request.session['name'] = request.POST['name']
        request.session['loc'] = request.POST['loc']
        request.session['lang'] = request.POST['lang']
        request.session['comment'] = request.POST['comment']
        return redirect("/results")
    else:
        return redirect("/")

def results(request):
    context = {
        'name' : request.session['name'],
        'location' : request.session['loc'],
        'language' : request.session['lang'],
        'comment' : request.session['comment'],
        'count' : request.session['count']
    }
    return render(request, 'forms/results.html', context)