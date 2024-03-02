the main entities (objects):

    categories:
        -name
        -number of books

    book:
        -title
        -auther
        -categoriy
        -published date
        -number of pages
        -hint
        -is valid
        -number of copies
        -buying price
        -borrowing price

    readers :
        -name 
        -ssd 
        -id
        -date of start join
        -date of end join
        -borrowed books (list)
        -history of borrowing

    transactions: (-borrow-buying)
        - reader id 
        - book name
        - date of transaction
        - date of end borrow (if it was borrw)
        - price

        (join for new reader):
        - add all details of reader object
        
        (add new book):
        - add all details of book object
        




