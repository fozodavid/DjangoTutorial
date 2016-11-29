from django.shortcuts import render_to_response, get_object_or_404
from blog.models import BlogPost


# Create your views here.
def view_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)    
    return render_to_response("blogpost.html", {'post' : post,})