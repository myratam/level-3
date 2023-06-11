from django.db import models

# Create your models here.
class Post(models.Model):
    """
    Model representing a blog post.

    Fields:
    - title (CharField): The title of the blog post.
    - body (TextField): The content of the blog post.
    - signature (CharField): The signature or quote associated with the blog post.
    - date (DateTimeField): The date and time of the blog post creation.

    Methods:
    - __str__: This returns the string representation of the blog post (the title).
    """
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="The future belongs to those who believe in the beauty of their dreams.")
    date = models.DateTimeField()

    def __str__(self):
        return self.title


