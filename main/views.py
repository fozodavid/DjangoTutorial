from django.shortcuts import render
from main.models import Article

# Create your views here.
def home(request):
    article = Article.objects.last()
    return render(request,'index.html',{'article':article,})