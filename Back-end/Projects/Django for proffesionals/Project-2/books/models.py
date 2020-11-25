import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Book(models.Model):
    id = models.UUIDField( # set id field to be a UUIDField that is now the primary key
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True) # used in templates/books/book_detail.html as book.cover.url 
    # If we wanted to allow uploads of a regular file rather than an image file the only difference could be to change ImageField to FileField.   

    class Meta:
        indexes = [ # new
            models.Index(fields=['id'], name='id_index'),
        ]

        # create custom permission: to read all books. In other words access to the DetailView. 
        permissions = [
            ("special_status", "Can read all books"),
        ]

    # __str__ method to control how the object is outputted in the Admin and Django shell.
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)]) # "{{ book.get_absolute_url }}", is same as "{% url 'book_detail' book.pk %}"


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews', # Set the name reviews to be the name of the entire Review model. in templates/books/book_detail.html 
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(), # refer to our CustomUser model
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review

    # in templates/books/book_detail.html 
    # since the reviews model is key we follow it by using book.reviews.all 