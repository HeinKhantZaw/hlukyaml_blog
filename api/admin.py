from django.contrib import admin

# Register your models here.
from api.models import Blog, Author

admin.site.register(Blog)
admin.site.register(Author)
