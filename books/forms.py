from django import forms
from .models import Book , Category

### form for books ###
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['slug']

### form for Category ###
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        
