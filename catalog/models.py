from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Наименование категории", help_text="Введите наименование категории")
    slug_name = models.SlugField(max_length=100, verbose_name="Slug-имя категории", help_text="Введите slug-имя категории", unique=True)
    image = models.ImageField(upload_to="product/category_image", verbose_name="Изображение категории", help_text="Загрузите изображение категории", blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Родительская категория")
    name = models.CharField(max_length=100, unique=True, verbose_name="Наименование подкатегории", help_text="Введите наименование подкатегории")
    slug_name = models.SlugField(max_length=100, verbose_name="Slug-имя подкатегории", help_text="Введите slug-имя подкатегории", unique=True)
    image = models.ImageField(upload_to="product/subcategory_image", verbose_name="Изображение подкатегории", help_text="Загрузите изображение подкатегории", blank=True, null=True)

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name="Подкатегория товара")
    name = models.CharField(max_length=100, unique=True, verbose_name="Наименование товара", help_text="Введите наименование товара")
    slug_name = models.SlugField(max_length=100, unique=True, verbose_name="Slug-имя товара", help_text="Введите slug-имя товара")
    price = models.PositiveIntegerField(verbose_name="Цена товара", help_text="Введите цену товара")
    image1 = models.ImageField(upload_to='product/product_image1', verbose_name="Изображение товара 1", help_text="Загрузите 1 изображение товара", blank=True, null=True)
    image2 = models.ImageField(upload_to='product/product_image2', verbose_name="Изображение товара 2", help_text="Загрузите 2 изображение товара", blank=True, null=True)
    image3 = models.ImageField(upload_to='product/product_image3', verbose_name="Изображение товара 3", help_text="Загрузите 3 изображение товара", blank=True, null=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
