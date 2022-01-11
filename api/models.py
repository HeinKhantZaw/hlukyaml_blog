from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.author_name


class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_cover = models.ImageField(upload_to='')
    blog_body = RichTextField()
    author = models.ForeignKey(Author, related_name='blog_author', on_delete=models.CASCADE, default='Anonymous')
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.blog_title
