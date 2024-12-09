class Library:
    book_list = []

    @classmethod
    def entry_book(cls,book):
        cls.book_list.append(book)


    @classmethod
    def view_all_books(cls):
        if not cls.book_list:
            print("No books available.")
        else:
            for book in cls.book_list:
                book.view_book_info()




class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = True
        Library.entry_book(self)

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"Book '{self.__title}' has been borrowed.")
        else:
            print(f"Book '{self.__title}'is already borrowed.")

    
    def return_book(self):
        if not self.__availability:
            self.__availability = True

            print(f"Book '{self.__title}'has been returned.")
        else:
              print(f"Book '{self.__title}'is not currently borrowed.")

    
    def view_book_info(self):
        availability_status="Available" if self.__availability else "Not Available"
        print(f"ID:{self.__book_id},Title:{self.__title}, Author:{self.__author},Availability:{availability_status}")
        

    def get_book_id(self):
        return self.__book_id
    

    def is_available(self):
        return self.__availability
    

    def menu():
        while True:
          print("\nLibrary Menu")
          print("1. View All Books")
          print("2. Borrow Book")
          print("3. Return Book")
          print("4. Exit")

          choice=input("Enter Your Choice: ")

          if choice=="1":
              if not Library.book_list:
                  print("No Books Available.")
            
              else:
                  for book in Library.book_list:
                      book.view_book_info()
             
          elif choice == "2":
              book_id = input("Enter The book ID to Borrow: ")
              for book in Library.book_list:
                  if book.get_book_id()==book_id:
                      book.borrow_book()
                      break
                  else: 
                     print("Invalid")


          elif choice == "3":
              book_id = input("Enter The book ID to return: ")
              for book in Library.book_list:
                  if book.get_book_id()==book_id:
                      book.return_book()
                      break
                  else:
                      print("Invalid")

          elif choice == "4":
              print("Exit")
              break
          else:
              print("Invalid.Please try again.")

book1= Book("001","phthon programming","Nabil")
book2= Book("002","Data Structures", "Shariful")
book3= Book("003","Algorithms", "Nahid")
Book.menu()

                  
          




       
       
               

                  


