from collections import namedtuple

# 1
Car = namedtuple('Cars', ('model', 'make', 'color', 'year'))
car1 = Car('BMW i5', 'BMW', 'White', 2019)
car2 = Car('Tesla Roadster', 'Tesla', 'Black', 2023)

# print(f'Model: {car1.model}, \nMake: {car1.make}, \nColor: {car1.color}, \nYear: {car1.year}')
# print(f'\nModel: {car2.model}, \nMake: {car2.make}, \nColor: {car2.color}, \nYear: {car2.year}')


#2
Book = namedtuple('Books', ("Title",'Author', 'Genre', 'price', 'pages'))
book1 = Book('Digital Fortress', 'Dan Brown', 'roman', '45.000', '400+')
book2 = Book('Harry Potter and half-blood prince', 'J.K.Rowling', 'book-series', '50.000', '320+')
# print(f'Title: {book1.Title}, \nAuthor: {book1.Author}, \nGenre: {book1.Genre}, \nPrice: {book1.price}, \nPages: {book1.pages}')
# print(f'\nTitle: {book2.Title}, \nAuthor: {book2.Author}, \nGenre: {book2.Genre}, \nPrice: {book2.price}, \nPages: {book2.pages}')


# 3
phone = namedtuple('Phone', ('model', 'make', 'memory', 'color', 'price'))
p1 = phone('iPhone 11 Pro', 'iPhone', '128 GB', 'pink', '$850')
p2 = phone('Samsung A04e', 'Samsung', '32 GB', 'ocean blue', '$200')

# print(f'Model: {p1.model}, \nMake: {p1.make}, \nMemory: {p1.memory}, \nColor: {p1.color}, \nPrice: {p1.price}')
# print(f'\nModel: {p2.model}, \nMake: {p2.make}, \nMemory: {p2.memory}, \nColor: {p2.color}, \nPrice: {p2.price}')

# 4
student = namedtuple('Student_info', ('name', 'surname', 'age', 'university', 'major'))
s1 = student('Zarnigor', 'Dekhonova', 18, 'UzJMCU', 'International Relations')
s2 = student('Zilola', 'Abdullayeva', 19, 'UWED', 'Jurisprudence')

print(f'Name: {s1.name}, \nSurname: {s1.surname}, \nAge: {s1.age}, \nUniversity: {s1.university}, \nMajor: {s1.major}')
print(f'\nName: {s2.name}, \nSurname: {s2.surname}, \nAge: {s2.age}, \nUniversity: {s2.university}, \nMajor: {s2.major}')