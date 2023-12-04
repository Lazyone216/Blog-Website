from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Posts, Category
from .forms import CommentForm


def home(request):
    posts = Posts.objects.filter(status=Posts.ACTIVE)
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def robots_txt(request):
    text = [
        "User-Agent: *",
        'Disallow: /admin/',
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")



def detail(request, category_slug, slug):
    post = get_object_or_404(Posts, slug=slug, status=Posts.ACTIVE)

    if request.method == 'POST':
        form = CommentForm(request.POST)


        if form.is_valid():
            comment = form.save(commit= False)
            comment.post = post
            comment.save()

            return redirect('post.detail', slug=slug)

    else:
        form = CommentForm()

    return render(request, 'blog/detail.html',{'post':post, 'form':form})

def category(request,slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Posts.ACTIVE)

    return render(request, 'blog/category.html',{'category': category, 'posts': posts})


def search(request):
    query = request.GET.get('query', '')

    posts = Posts.objects.filter(status=Posts.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(content__icontains=query))
    return render(request, 'blog/search.html', {'posts':posts, 'query':query})

# Create your views here.
