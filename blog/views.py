from django.shortcuts import render
from django.http import HttpResponse

# Fake data

posts = [
    {
        'author': 'Takie',
        'title': 'Title1',
        'content': 'qsdmklgjqsdmlkgjqsmdlgkjqdsg',
        'date_posted': 'August 9, 1995'
    },
    {
        'author': 'Takie',
        'title': 'Title2',
        'content': 'qsdmklgjqsdmlkgjqsmdlgkjqdsg',
        'date_posted': 'August 9, 1995'
    }, {
        'author': 'Takie',
        'title': 'Title3',
        'content': 'qsdmklgjqsdmlkgjqsmdlgkjqdsg',
        'date_posted': 'August 9, 1995'
    }
]


# Create your views here.

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
