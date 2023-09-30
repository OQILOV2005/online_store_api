from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone  = models.CharField(max_length=13, unique=True, blank=True, null=True)
    avatar = models.ImageField(upload_to='user_avatar', blank=True, null=True)


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Product(models.Model):
    name = models.CharField(max_length=55)
    photo = models.ManyToManyField(to='ProductImage')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    barnd = models.ForeignKey(to="Brand", on_delete=models.CASCADE)
    sub_category = models.ForeignKey(to='Sub_Category', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_sale = models.BooleanField(default=False)
    sale = models.IntegerField(default=0)
    description = models.TextField()
    addition = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(to='Tag')
    is_credit = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    like_number = models.IntegerField(default=0)
    status_size = models.IntegerField(null=True, blank=True, choices=
    (
        (1,"kg"),
        (2,"dona"),
        (3,"metr"),
        (4,"pachka"),
        (5,"blok")
    )
    )

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    name = models.CharField(max_length=25)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/')



class Card(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(to=Product)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    comment = models.ForeignKey(to='Comment', on_delete=models.CASCADE, null=True, blank=True, related_name='reply')
    text = models.TextField(verbose_name='izoh')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Saved(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Maxsuloti')

    def __str__(self):
        return self.product.name


class Region(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(to=User, blank=False, verbose_name="Mijoz", on_delete=models.CASCADE)
    product = models.ManyToManyField(to=Product,)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    is_delivery = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_credit = models.BooleanField(default=False)
    period = models.IntegerField(default=12, null=True, blank=True)

    def __str__(self):
        return self.user.username

















