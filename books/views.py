from django.shortcuts import render , redirect
from .models import Category , Book
from .forms import BookForm , CategoryForm
from .filters import BookFilter

## get all categories from models ###
categories = Category.objects.all()

### function to filter ###
 

### function to add new category ###
def add_category(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
    else:
        category_form = CategoryForm()
    return category_form

### view to show all books ###
def show_books(request):
    ## get all books from models ###
    all_books = Book.objects.all()
    ## filter on books by name ##
    filter = BookFilter(request.GET, queryset=all_books)
    ## override on all_books variable ##
    all_books = filter.qs
    ### for adding category ###
    category_form = add_category(request)
    ## get all categories from models ###
    categories = Category.objects.all()
    ## context that will be passed ##
    context = {'books':all_books , 'categories':categories,'category_form':category_form , 'filter':filter}

    return render(request,'books.html',context)

### view that edit a book attribute ###
def edit_book(request, id):
    ## get book by id ##
    book = Book.objects.get(id=id)
    ### for adding category ###
    category_form = add_category(request)
    ### check if request method is post or get ###
    if request.method == 'POST':
        form = BookForm(request.POST , request.FILES , instance=book )
        if form.is_valid():
            form.save()
            return redirect('all_books')
    else:
        form = BookForm(instance=book )
    ## context that will be passed ##
    context = {'form':form , 'categories':categories,'category_form':category_form}

    return render(request, 'edit.html',context)

# ### view that add new book ###
# def add_new_book(request):
#     ### check if request method is post or get ###
#     if request.method == 'POST':
#         form = BookForm(request.POST , request.FILES  )
#         if form.is_valid():
#             form.save()
#             return redirect('all_books')
#     else:
#         form = BookForm()
#     ## context that will be passed ##
#     context = {'form':form , 'categories':categories}

#     return render(request, 'add_book.html',context)

### view that delet a book from models ###
def delete_book(request,id):
    book = Book.objects.get(id=id)
    ### for adding category ###
    category_form = add_category(request)
    ### check if request method is post ###
    if request.method == 'POST':
        ## delete book from models
        book.delete()
        ## return to all books page ## 
        return redirect('all_books')
    ## context that will be passed ##
    context = {'book':book, 'categories':categories,'category_form':category_form}
    return render(request,'delete.html',context)

### view to show home page ###
def show_home(request):
    ## queryset to get all books ###
    all_books = Book.objects.all()
    ## filter on books by name ##
    filter = BookFilter(request.GET, queryset= all_books)
    ## override on all_books variable ##
    all_books = filter.qs
    ### for adding category ###
    category_form = add_category(request)
    ## get number of whole books in data base ##
    books_number = Book.objects.count()
    ## get all categories from models ###
    categories = Category.objects.all()
    ### check if request method is post or get ###
    if request.method == 'POST':
        form = BookForm(request.POST , request.FILES  )
        if form.is_valid():
            form.save()
            return redirect('all_books')
    else:
        form = BookForm()
    ## context to pass to html file 
    context = {'books':all_books , 'categories': categories , 'number':books_number,'form':form ,'category_form':category_form,'filter':filter}

    return render(request, 'home.html',context)
