from django.shortcuts import render, redirect
from article.models import Article, Comment
from datetime import datetime


# Create your views here.

def index(request):
    articles = Article.objects.all()
    return render(request,'index.html',{'articles':articles})

def show(request, pk):
    article = Article.object.get(pk=pk)
    return render(request, 'show.html',{'article':article})

#def new(request):
#    return render(request, 'new.html')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'edit.html', {"article":article})

def create(request):
    if request.method=='POST':
        article = Article()
        article.author = request.user
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
        return redirect('article:show', pk=article.pk)
    else:
        return render(request, 'new.html')
    
def update(request, pk):
    article = Article.objects.get(pk=pk)
    
#    if 
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
    return redirect('article:show', pk=article.pk)

def delete(request, pk):
    article = Article.object.get(pk=pk)
    if article.author == request.user:
        article.delete()
    return redirect('article:index') 
    

def create_comment(request, pk):
    if request.method == 'POST':
        comment = Comment()
        comment.article = Article.objects.get(pk=pk)
        comment.author = request.user
        comment.content = request.POST['content']
        comment.created_at = datetime.now()
        comment.save()

    return redirect('article:show', pk=pk)

def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    if comment.author == request.user:
       comment.delete()
    return redirect('article:show', pk=pk)