from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def blog_home(request):
    """
    The view function for the blog homepage.

    This view displays a list of all blog posts.
    Only authenticated users can access this page.

    Parameters:
    - request: HttpRequest object representing the current request.

    Returns:
    - HttpResponse object rendering the 'blog.html' template,
      including the list of blog posts as context.

    """
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})
