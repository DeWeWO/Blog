from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Category(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        return super().save( *args, **kwargs)
    
    class Meta:
        db_table = "category"
        verbose_name_plural = "Categories"

class Post(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name="posts")
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts")
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        return super().save( *args, **kwargs)
    
    class Meta:
        ordering = ["-id"]
        db_table = "posts"

class PostImage(BaseModel):
    image = models.ImageField(upload_to="posts/")
    post = models.ForeignKey(to="core.Post", on_delete=models.CASCADE, related_name="images")
    
    class Meta:
        db_table = "post_image"
