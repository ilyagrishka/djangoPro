from django.forms import ModelForm, BooleanField,ValidationError
from catalog.models import Product, Version



class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("views_counter", "owner")


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = ("description", "name")

    def clean_first_name(self):
        cleaned_data = self.cleaned_data.get('name', "description")
        list_of_word = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]
        for word in list_of_word:
            if word in cleaned_data:
                raise ValidationError('Ошибка, связанная с применением запрещённых слов')

        return cleaned_data


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
