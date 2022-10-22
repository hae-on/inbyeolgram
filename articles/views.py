from django.shortcuts import render,redirect

from articles.forms import ArticleForm

# Create your views here.

def index(request):
    return render(request, 'articles/index.html')

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.save()
            return redirect("articles:index")
    else:
        article_form = ArticleForm()

    context = {
        "article_form": article_form,
    }

    return render(request, 'articles/form.html', context)