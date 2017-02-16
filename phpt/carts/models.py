from PIL import Image
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=120,  blank=False)
    slug = models.SlugField(default="categ")

    def __str__(self):
        return self.name

CARTS_COLORS = (
    ('Red', 'Red'),
    ('Green', 'Green')
)

_MAX_SIZE = 100

def get_deleted_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Carts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_deleted_user))
    category = models.ForeignKey("Category")
    cart_color = models.CharField(max_length=5, choices=CARTS_COLORS, default='Red')
    title = models.CharField(max_length=120)
    developer = models.CharField(max_length=120)
    img = models.ImageField(height_field='img_height', width_field='img_width', blank=True, verbose_name="Изображение товара")
    img_height = models.PositiveIntegerField(default=200)
    img_width = models.PositiveIntegerField(default=200)
    place = models.CharField(max_length=100)
    comment = models.TextField()
    is_public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("carts_detail", kwargs={"category_slug": self.category.slug, "pk": self.pk})

    def save(self, *args, **kwargs):
        # Сначала - обычное сохранение
        super(Carts, self).save(*args, **kwargs)

        # Проверяем, указан ли логотип
        if self.img:
            filename = self.img.path
            width = self.img.width
            height = self.img.height

            max_size = max(width, height)

            # Может, и не надо ничего менять?
            if max_size > _MAX_SIZE:
                # Надо, Федя, надо
                image = Image.open(filename)
                # resize - безопасная функция, она создаёт новый объект, а не
                # вносит изменения в исходный, поэтому так
                image = image.resize(
                    (round(width / max_size * _MAX_SIZE),  # Сохраняем пропорции
                    round(height / max_size * _MAX_SIZE)),
                    Image.ANTIALIAS
                )
                # И не забыть сохраниться
                image.save(filename)
