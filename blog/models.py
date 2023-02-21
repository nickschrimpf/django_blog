from django.db import models
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    name = models.CharField( max_length=20)

    def __str__(self) -> str:
        return f"{self.name}"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Post(models.Model):
    title = models.CharField(max_length=150)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, verbose_name="Author", on_delete=models.SET_NULL,null=True, related_name="posts")
    date = models.DateField(auto_now_add=True)
    excerpt = models.CharField(max_length=200)
    image = models.CharField(max_length=50)
    content = models.TextField(validators=[MinLengthValidator(100)])
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.title} {self.date}"
    



