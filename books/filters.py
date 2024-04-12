import django_filters
from .models import Book

### filter for book by name ###
class BookFilter(django_filters.FilterSet):
    ## cascade on name to get what is in contain of search ##
    name = django_filters.CharFilter(lookup_expr='icontains') 

    ## specify model that filter on its object ##
    class Meta:
        model = Book
        fields = ['name'] 


