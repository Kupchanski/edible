from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=120,  blank=False)

    def __str__(self):
        return self.name

CARTS_COLORS = (
    ('Red', 'Red'),
    ('Green', 'Green')
)

def get_deleted_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Carts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_deleted_user))
    category = models.ForeignKey("Category")
    cart_color = models.CharField(max_length=5, choices=CARTS_COLORS, default='Red')
    title = models.CharField(max_length=120)
    img = models.ImageField(height_field='img_height', width_field='img_width', blank=True, verbose_name="Изображение товара")
    img_height = models.PositiveIntegerField(default=200)
    img_width = models.PositiveIntegerField(default=200)
    place = models.CharField(max_length=100)
    comment = models.TextField()
    is_public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title