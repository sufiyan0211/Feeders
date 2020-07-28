from django.shortcuts import render
from core.models import Info, Covid, News, Business, Technology, Educations, Fasion, Movies, Series

# Create your views here.
def index(request):
    return render(request, 'index.html')


def sports(request):
    objs = Info.objects.all()
    context = {
        'objs' : objs
    }
    return render(request, 'sports.html',context)


def covid(request):
    objs = Covid.objects.all()
    context = {
        'objs' : objs
    }
    return render(request, 'covid.html',context)


def news(request):
    objs = News.objects.all()
    context = {
        'objs' : objs
    }
    return render(request, 'news.html',context)


def business(request):
    objs = Business.objects.all()
    context = {
        'objs' : objs
    }
    return render(request, 'business.html',context)


def technology(request):
    objs = Technology.objects.all()
    context = {
        'objs' : objs
    }
    return render(request, 'technology.html',context)


def educations(request):
    objs = Educations.objects.all()
    context = {
        'objs' : objs
    }
    return render(request, 'educations.html',context)


def fasion(request):
    objs = Fasion.objects.all()
    context = {
        'objs' : objs
    }
    return render(request, 'fasion.html',context)


def movies(request):
    objs = Movies.objects.all()
    context = {
        'objs' : objs
    }
    return render(request, 'movies.html',context)


def series(request):
    objs = Series.objects.all()
    context = {
        'objs' : objs
    }
    return render(request, 'series.html',context)
