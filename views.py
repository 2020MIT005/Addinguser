from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.
from django.shortcuts import render, HttpResponseRedirect, Http404, get_object_or_404

# Create your views here.
def index(request):

    
    posts = Project.objects.all()
    

    if request.method == "POST":
        
       
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = Project()
            post.name = form.cleaned_data["name"]
            post.image1 = form.cleaned_data["image1"]
            post.image2 = form.cleaned_data["image2"]
            post.image3 = form.cleaned_data["image3"]

            
            post.save()

            return redirect('index')
    else:
        form = ProjectForm()

            
    return render(request, "app/index.html", {   
        'form':form,
        'posts':posts,

    })