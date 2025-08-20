# forms.py
from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, HTML
from django.forms import ModelChoiceField

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            return [single_file_clean(d, initial) for d in data]
        return single_file_clean(data, initial)

class PostForm(forms.ModelForm):
    images = MultipleFileField(
        label='Post uchun rasm(lar)', 
        required=True,
        widget=MultipleFileInput(attrs={
            'class': 'form-control image-input',
            'id': 'id_images'
        })
    )

    class Meta:
        model = Post
        fields = ["title", "description", "category", "author"]
        labels = {
            "title": "Sarlavha",
            "description": "Tavsif",
            "category": "Kategoriya",
            "author": "Muallif",
        }
        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Sarlavha kiriting",
                "class": "form-control"
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "To'liq tavsifni yozing",
                "rows": 4,
                "class": "form-control"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if isinstance(self.fields.get("category"), ModelChoiceField):
            self.fields["category"].empty_label = "--- Kategoriya tanlang ---"
            
        self.fields["title"].widget.attrs.update({
            "title": "Sarlavha uchun joy"
        })
        
        self.fields["description"].widget.attrs.update({
            "title": "Postni to'liq yozing"
        })
        
        self.fields["category"].widget.attrs.update({
            "title": "Post qaysi sohaga tegishli",
            "class": "form-control"
        })

        self.fields["author"].widget.attrs.update({
            "class": "form-control"
        })

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_enctype = "multipart/form-data"
        self.helper.layout = Layout(
            Field("title"),
            Field("description"),
            Field("category"),
            Field("author"),
            Field("images"),
            HTML('<div class="d-flex justify-content-end mt-3">'),
            Submit('submit', 'Postni Yuklash', css_class='btn btn-custom'),
            HTML('</div>')
        )