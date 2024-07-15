from pprint import pprint

from django.core.management.base import BaseCommand
from catalog.models import Category, Product
import json
from django.conf import settings
import os


class Command(BaseCommand):
    help = "загрузка данных в базу"

    @staticmethod
    def clear_all_data():
        Category.objects.all().delete()
        Product.objects.all().delete()

    def handle(self, *args, **options):

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(**category["fields"])
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            cat_id = product["fields"]["category"]
            print(cat_id)
            product["fields"]["category"] = Category.objects.get(pk=cat_id)
            product_for_create.append(
                Product(**product["fields"])
            )

        Product.objects.bulk_create(product_for_create)

    @staticmethod
    def json_read_categories():
        data = Command.read_json()
        return list(filter(lambda x: x.get("model") == "catalog.category", data))

    @staticmethod
    def json_read_products():
        data = Command.read_json()
        return list(filter(lambda x: x.get("model") == "catalog.product", data))

    @staticmethod
    def read_json():
        path = str(settings.BASE_DIR) + "/catalog/fixture/data.json"
        # path = os.path.join(settings.BASE_DIR, "/catalog/fixture/catalog.json")
        with open(path, "r",encoding="utf-8") as file:
            data = json.load(file)
            return data
