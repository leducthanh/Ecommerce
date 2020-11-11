from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save

from ecommerce.utils import unique_slug_generator, get_filename

# Create your models here.

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) |
                  Q(description__icontains=query) |
                  Q(price__icontains=query)
                  )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self): #Product.objects.featured()
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)



class Product(models.Model):
    title           = models.CharField(max_length = 100)
    slug            = models.SlugField(blank = True, null = True)
    description     = models.TextField()
    price           = models.DecimalField(default=0, max_digits=6, decimal_places=1)
    image           = models.ImageField(upload_to = "products/",blank = True, null = True)
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default = True)
    created_at      = models.DateTimeField(auto_now_add = True)

    objects = ProductManager()

    def get_absolute_url(self):
        return "/products/{slug}/".format(slug=self.slug)

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    instance.cart.all

pre_save.connect(product_pre_save_receiver, sender=Product)
