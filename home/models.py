from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField()
    bio = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=100)


    def save(self, *args, **kwargs):
        if not self.slug or self.slug.strip() == '':
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True, related_name='book_author')
    vol_type = models.CharField(max_length=50)
    summary_story = models.TextField(blank=True)
    publications = models.CharField(max_length=100, blank=True)
    number_of_page = models.IntegerField()
    publish_year = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(datetime.date.today().year)],verbose_name='publish_year', blank=True )
    edition = models.CharField(max_length=50, blank=True)
    book_code = models.IntegerField(blank=True)
    translator = models.CharField(max_length=50, blank=True)
    categories = models.ManyToManyField(Category, related_name='book_categories', blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.slug.strip() == '':
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title