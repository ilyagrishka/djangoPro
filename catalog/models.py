from django.db import models

from users.models import User
from django.contrib.auth.mixins import UserPassesTestMixin


class Product(models.Model, UserPassesTestMixin):

    name = models.CharField(
        max_length=100,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        max_length=100,
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
    )
    photo = models.ImageField(
        upload_to="product/photo",
        verbose_name="Фото",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey("Category",
                                 on_delete=models.SET_NULL, blank=True, null=True, related_name="products"
                                 )
    price = models.IntegerField(
        verbose_name="Цена продукта", help_text="Введите цену продукта"
    )
    created_at = models.DateTimeField(
        blank=True, verbose_name="Дата создания", help_text="Введите дату загрузки",
        auto_now_add=True

    )
    updated_at = models.DateTimeField(
        blank=True, verbose_name="Дата последнего изменения", help_text="Введите дату",
        auto_now=True
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0
    )
    owner = models.ForeignKey(User, verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL)
    publication_status = models.BooleanField(default=False, verbose_name="статус публикации")

    def test_func(self):
        return self.user.is_superuser

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]
        permissions = [
            ("can_edit_product", "can edit product"),
            ("can_edit_description", "can edit description"),
            ("can_change_category", "can change category")
        ]

    def __str__(self):
        return f"{self.name}-{self.description}"


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    description = models.TextField(
        max_length=100,
        verbose_name="Описание категории",
        help_text="Введите описание категории",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}-{self.description}"


class BlogNote(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Запись",
        help_text="Введите новую запись",
    )
    slug = models.CharField(
        max_length=150,
        unique=True,
        db_index=True,
        verbose_name="URL")

    description = models.TextField(
        max_length=100,
        verbose_name="Описание",
    )
    photo = models.ImageField(
        upload_to="product/photo",
        verbose_name="Фото",
        help_text="Загрузите новое фото",
    )

    created_date = models.DateTimeField(
        blank=True, verbose_name="Дата создания", help_text="Введите дату загрузки",
        auto_now_add=True

    )

    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0
    )
    publication_status = models.BooleanField(default=False,

                                             )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["name", "description"]

    def __str__(self):
        return f"{self.name}-{self.description}"


class Version(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        verbose_name='версия')

    version_number = models.PositiveIntegerField(
        verbose_name="номер версии",
        default=0
    )

    version_name = models.CharField(
        max_length=100,
        verbose_name="номер версии",
    )

    version_bull = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["product"]

    def __str__(self):
        return f"{self.product}-{self.version_name}"
