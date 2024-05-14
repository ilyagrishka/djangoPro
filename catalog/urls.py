from django.urls import path, include
from catalog.apps import AppConfig
from views import home, contacts

app_name = AppConfig.name

urlpatterns = [
    path("", home, name="home")
]

urlpatterns1 = [
    path("", contacts, name="contacts")
]
