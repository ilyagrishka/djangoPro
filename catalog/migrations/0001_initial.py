from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название категории",
                        max_length=100,
                        verbose_name="Название категории",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание категории",
                        max_length=100,
                        verbose_name="Описание категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название продукта",
                        max_length=100,
                        verbose_name="Название продукта",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание продукта",
                        max_length=100,
                        verbose_name="Описание продукта",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        help_text="Загрузите фото продукта",
                        upload_to="product/photo",
                        verbose_name="Фото",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        help_text="Введите цену продукта", verbose_name="Цена продукта"
                    ),
                ),
                (
                    "date_create",
                    models.DateTimeField(
                        blank=True,
                        help_text="Введите дату загрузки",
                        verbose_name="Дата создания",
                    ),
                ),
                (
                    "date_last_change",
                    models.DateTimeField(
                        blank=True,
                        help_text="Введите дату",
                        verbose_name="Дата последнего изменения",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="catalog.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["name", "price"],
            },
        ),
    ]
