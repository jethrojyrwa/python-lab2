def addBook(books,isbn,title,author,publisher,volume,year):
    if isbn in books:
        print(f"Book with ISBN {isbn} already exists.")
        return books
    books[isbn] = {"title":title,"author":author,"publisher":publisher,"volume":volume,"year_of_publication":year}
    print(f"Successfully added book with ISBN: {isbn}")
    return books

def removeBook(books,isbn):
    if isbn in books:
        del books[isbn]
        print(f"Successfully deleted book with ISBN: {isbn}")
    else:
        print(f"Book with ISBN {isbn} does not exist")
    return books

def displayBook(books,isbn):
    if isbn in books:
        print(f"ISBN: {isbn}")
        print("Title: ",books[isbn]['title'])
        print("Author(s): ",books[isbn]['author'])
        print("Volume: ",books[isbn]['volume'])
        print("Year of Publication: ",books[isbn]['year_of_publication'])
        print()
    else:
        print(f"Book with {isbn} does not exist")

def searchBook(books,var):
    found = False
    for isbn in books:
        if books[isbn]['title'] == var or books[isbn]['author'] == var:
            print(f"Book with title/author '{var}' and ISBN: {isbn} exists in the library")
            displayBook(books, isbn)
            found = True
            
    if not found:
        print(f"Book with title/author '{var}' does not exist in the library")
    return

def listBooks(books):
    for isbn in books.keys():
        displayBook(books,isbn)

def updateBook(books,isbn,title,author,publisher,volume,year):
    if isbn in books:
        books[isbn]['title'] = title
        books[isbn]['author'] = author
        books[isbn]['publisher'] = publisher
        books[isbn]['volume'] = volume
        books[isbn]['year_of_publication'] = year
        print(f"Successfully updated details of book with ISBN {isbn}")
        print("New Details of the book:")
        displayBook(books,isbn)
    else:
        print(f"Book with ISBN {isbn} does not exist")
    return books
    
def searchByISBN(books,isbnS):
    if isbnS in books:
        print(f"Book with ISBN {isbnS} is available in the library")
        displayBook(books, isbnS)
    else:
        print(f"Book with ISBN {isbnS} is not available in the library")
    return




