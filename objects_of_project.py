####### creating all objects of the system ########

from datetime import date , timedelta
from random import randint

##### object of category #####
class Category:
    #### constructor of object ####
    def __init__(self,category_title):
        self.category_title = category_title

### object for book ###
class Book(Category):
    #### constructor of object ####
    def __init__(self,title,auther,number_pages,published_date,category_title,number_copies,borrowing_price,buying_price,is_valid=True):
        self.title = title
        self.auther = auther
        self.number_pages = number_pages
        self.published_date = published_date
        self.number_copies = number_copies
        self.borrowing_price = borrowing_price
        self.buying_price = buying_price
        self.is_valid= is_valid
        super().__init__(category_title) ### inherit category title from category object

    ## to show book title if book called
    def __str__(self):
        return f"{self.title}"

    ### decreases number of valid (borrowed or bought) books if copy got borrowed ###
    def borrowed(self):
        self.number_copies -= 1

    ### check validation of bbok ###
    def check_validation(self):
        if self.number_copies == 0:
            self.is_valid = False
        return self.is_valid

### object for readers ####
class Reader:
    ### list cosists of all readers ids ###
    all_ids = []
    ### list cosists of readers objects ###
    all_readers = []
    ########## constructor ###########
    def __init__(self,name,ssd):
        self.name = name
        self.ssd = ssd
        self.date_of_joining =  date.today()
        self.date_of_end_joining = self.date_of_joining + timedelta(days=30)
        self.id = Reader.generate_id()
        Reader.all_ids.append(self.id)
        Reader.all_readers.append(self) ### append object in list
    
    #### method to create ids automaticlly to each user
    @classmethod
    def generate_id(cls):
        id = ''
        for i in range(6):
            id += str(randint(1,9))
        ### check if id is already exists or not
        if id in cls.all_ids:
            ### if yes recursive method again
            cls.generate_id()
        else:
            return id
        
    ### get id method by name ###
    @classmethod
    def get_id(cls,name):
        # get all readers  
        all_readers = cls.all_readers
        ## looping in all readers
        for reader in all_readers:
            if reader.name == name:
                return reader.id
            else:
                return "name not exists"
        
###### class for each reader transaction ########
class Transaction(Reader,Book):
    ### constructor ###
    def __init__(self, name, title):
        self.date_of_transaction = date.today()
        Reader.__init__(self,name,None)
        self.id = Reader.get_id(self.name)
        Book.__init__(self,title,None,None,None,None,None,None,None,None,None)
    
    ### method get end date of 30 dayes of borrowing if transaction is borrowing
    @property
    def get_end_of_borrow(self):
        end_date = self.date_of_transaction + timedelta(days=30) 
        return end_date

