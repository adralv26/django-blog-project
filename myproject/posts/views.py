from django.shortcuts import render, redirect
from .models import Post
from .forms import CustomPost
# from django.http import HttpResponse

# Create your views here.
def posts_list(request):
    # posts = Post.objects.all()
    posts = Post.objects.all().order_by('date')
    context = {
        'active_link': 'posts',
        'posts':posts
    }
    return render(request,'posts/posts_list.html', context)
def post_page(request, slug):
    # return HttpResponse(slug)
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html',{'post':post} )

def post_form(request):
    if request.method == 'POST':
        form = CustomPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = CustomPost()
            
    for field in form.fields.values():
        field.widget.attrs["class"] = "form-control"
    context = {"form": form}
    return render(request, 'posts/post_form.html', context)