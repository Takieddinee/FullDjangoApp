from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['date_posted']


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    success_url = '/'
    model = Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
