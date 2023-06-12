from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def blog_home(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})
    """
    Display the blog homepage.

    This view function retrieves all blog posts and renders them on the blog homepage template.
    Only authenticated users can access this page.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: A response object rendering the 'blog.html' template, including the list
      of blog posts as context.

    Raises:
    - AuthenticationError: If the user is not authenticated.

    Note: This view function requires the user to be logged in.
    """
    

