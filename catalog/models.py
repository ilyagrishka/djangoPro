from django.db import models


class Product(models.Model):
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

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]

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

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["name", "description"]

    def __str__(self):
        return f"{self.name}-{self.description}"
