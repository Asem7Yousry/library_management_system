from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

### function to check if string is in arabic or not ###
def is_arabic(text):
    arabic_range = (0x0600, 0x06FF)  # Unicode range for Arabic characters
    for char in text:
        if arabic_range[0] <= ord(char) <= arabic_range[1]:
            return True
    return False

### function to slug arabic strings ###
def arabic_slugify(value):
    # Convert Arabic characters to their closest ASCII representation
    ascii_value = unidecode(value)
    # Use Django's built-in slugify function on the converted value
    return slugify(ascii_value)

### model for category ###
class Category(models.Model):
    title = models.CharField(max_length= 50)
    slug = models.SlugField(null=True, blank=True)

    ### to show category with its title ###
    def __str__(self) -> str:
        return f'{self.title}'
    
    ### override on save metod ###
    def save(self, *args , **kwargs):
        if not self.slug:
            ### check if self.title is arabic or not 
            if is_arabic(self.title):
                self.slug = arabic_slugify(self.title)
            else:
                self.slug = slugify(self.title)
        super().save(*args, **kwargs)

### all status of books ####
BOOK_STATUS = (
    ('Available','Available'),
    ('Sold','Sold'),
    ('Rented','Rented'),
)

### image method that name the book or ather image ####
def image_method_book(instance, filename):
    ### split file name to name and extention ####
    image_name , extention = filename.split('.')
    ### save image with it instance name and extention ####
    return f'books/{instance}.{extention}'

### image method that name the book or ather image ####
def image_method_auther(instance, filename):
    ### split file name to name and extention ####
    image_name , extention = filename.split('.')
    ### save image with it instance name and extention ####
    return f'auther/{instance.auther}.{extention}'

### model for book ###
class Book(models.Model):
    name = models.CharField(max_length= 50)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    auther = models.CharField(max_length=50)
    book_image = models.ImageField(upload_to= image_method_book , null=True , blank= True)
    auther_image = models.ImageField(upload_to= image_method_auther , null=True , blank= True)
    price = models.FloatField()
    pages_number = models.IntegerField()
    retal_price_day = models.FloatField(null= True , blank= True)
    retal_period = models.IntegerField(null= True , blank= True)
    status = models.CharField(max_length=30,choices= BOOK_STATUS ,default= 'Available', null=True , blank= True)
    slug = models.SlugField(null=True, blank=True)
    
    ### to show category with its name ###
    def __str__(self) -> str:
        return f'{self.name}'
    
    ### override on save metod ###
    def save(self, *args , **kwargs):
        if not self.slug:
            ### check if self.title is arabic or not 
            if is_arabic(self.name):
                self.slug = arabic_slugify(self.name)
            else:
                self.slug = slugify(self.name)
        super().save(*args, **kwargs)
