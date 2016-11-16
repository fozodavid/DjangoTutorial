from django.http import HttpResponseRedirect
from django.shortcuts import render
from main.models import Article
from main.forms import SurveyForm


# Create your views here.
def home(request):
    article = Article.objects.last()
    return render(request,'index.html',{'article':article},)

def form(request):
    form = SurveyForm()

    def redirection(subscription):
        if subscription:
            return HttpResponseRedirect('/subscribed/')
        else:
            return HttpResponseRedirect('/thanks/')

    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            return redirection(form.cleaned_data['subscription'])
    else:
        form = SurveyForm()

    return render(request,'form.html',{'form': form},)

def subscribed(request):
    return render(request,'subscribed.html')

def thanks(request):
    return render(request,'thanks.html')
