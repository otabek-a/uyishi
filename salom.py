class Book:
    book_count=0
    def __init__(self,title,author,genre,publicatio_year,price,availabilty):
        self.title=title
        self.author=author
        self.genre=genre
        self.publicatio_year=publicatio_year
        self.__price=price
        self.__availabilty=availabilty
        Book.book_count+=1
    def get_price(self):
        return self.__price
    def set_price(self,new_price):
        if new_price<0:
            raise ValueError('manfiy sonlarni kirsatish mumkin emas')
        self.__price=new_price
        return new_price
    def is_available(self):
        return self.__availabilty
    def set_available(self):
        return not self.__availabilty
    def about_book(self):
        print(f'this book name is { self.title} written by {self.author} in {self.publicatio_year} thi book genre is {self.genre} it costs {self.get_price()} and this book we have/not {self.is_available()}')
    def discount(self):
        return f'we can reduse our cost to 10% it should be {self.get_price()}={self.get_price()-((self.get_price()*10)/100)}'
    def Mark(self,mark=False):
        self.__availabilty=mark
        return self.__availabilty
    def get_book_count(self):
        x= self.book_count
        return f'we have total {x} objects'
book1=Book('harry potter','me','Fiction',1990,12,True)
book1.get_price()
book1.set_price(130000)
book1.is_available()
print(book1.set_available())
book1.about_book()
book1.discount()
x=book1.Mark()
print(x)
print(book1.get_book_count())
