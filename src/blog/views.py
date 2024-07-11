from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_blog(request):
    return render(request, 'index_blog.html')

def article(request,numero_article):
    if numero_article in ["01","02","03"]:
        return render(request, f'article_{numero_article}.html')
    else:
        return render(request, 'article_not_found.html')

