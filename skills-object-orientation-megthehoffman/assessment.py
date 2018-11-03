"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The three main design advantages that object orientation provides are: encapsulation,
   abstraction, and ploymorphism (which is related to inheritance). Encapsulation means that
   the pieces of our code that utilize certain functionality are close in proximity to that 
   functionality. This helps us to avoid "spaghetti code" and makes our code more readable.
   Abstraction means that we are able to organize and hide the pieces of our code that are not
   relevant to the understanding and usage of the main program. That is, we can hide how a method
   works and still use the method. Lastly, polymorphism allows us to make different types of
   objects within the same class. We do this mostly through instance attributes and inheritance.
   Instance attributes permit specific attributes that may only be relevant to one instance of a
   class object to be encapsulated in that instance (thereby also keeping it away from instances
   for whom the attribute is irrelevant). Inheritance allows us to create children from parent
   classes, which can be modified and made specifically separate via instance attributes.

2. What is a class?

    A class is a constructed data type that allows for the above advantages of object oriented
    programming. It is more structured and slightly less flexible than a dictionary.Examples of 
    classes include lists, tuples, and files. Classes can also be created and customized for 
    specific instances. 

3. What is a method?

    A method is a function that is defined on a specific class, and always has at least one
    parameter, self.  

4. What is an instance in object orientation?

    An instance is a individual occurence of a class. For example, if Fruit was a class, Melons
    might be one instance of Fruit. Instances may have attributes that are unique from the 
    parent Animal class, and there can be more than one instance of a class.

5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is an attribute that pertains to every object in the class. An instance 
   attribute is an attrubte that is relevant to a specific instance of a class, but not relevant 
   to other instances of the class or the class as a whole. Instance attributes can replace 
   class attributes, and can also add additional attributes to those already specified in a 
   class. For example, a class called Melons might have an attribute called shape that is set to
   'Round,' because that is true for all Melons. Within each instance of Melons, however, there
   may be different attributes that are specified, such as watermelon.color = 'Pink.' That
   attribute is not true for all instances of Melons.

"""


# Part 2: Road Class
# #############################################################################

class Road(object):
    """A Road object."""
    num_lanes = 2
    speed_limit = 25

    def __init__(self):
        pass

road_1 = Road()
road_2 = Road()

road_1.num_lanes = 4
road_1.speed_limit = 60


# Part 3: Update Password
# #############################################################################
class User(object):
    """A user object."""

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def update_password(self, password, new_password):
        if password != self.password:
            print('Invalid password')
        else:
            self.password = new_password


# Part 4: Build a Library
# #############################################################################
class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

# book = Book("Hello", "Goodbye")
# print(book)
# print(book.title)

class Library(object):
    """A Library object."""

    def __init__(self):
        self.books = []


    def add_book(self, title, author):
        """Adds book to list of books."""
        book = Book(title, author)
        self.books.append(book)


# lib = Library()
# book = Book("Hey", "There")
# lib.books.append(book)
# print(lib.books)

# REMEMBER TO USE self. 
# Need to pass self into class methods if I want it to recognize the instance


    def find_books_by_author(self, author):
        """Finds other books in the library by the same author."""
        for book in self.books:
            if book.author == author:
                list_books_by_author = []
                list_books_by_author.append(book)
                return list_books_by_author



# # Part 5: Rectangles
# # #############################################################################

class Rectangle(object):
    """A rectangle object."""

    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)


    def calculate_area(self):
        """Return the rectangle's area (length * width)."""
        return self.length * self.width


class Square(Rectangle):
    """A square object."""

    def __init__(self, square_size):
        self.length = float(square_size)
        self.width = float(square_size)
        super().__init__(self.length, self.width)

        # ALTERNATIVE METHOD that seems to work, maybe cleaner, not sure?
        # super().__init__(square_size, square_size)


    def calculate_area(self):
        if self.length == self.width:
            # Why does calculate.area take no arguments?
            return super().calculate_area()
        else:
            print('Invalid Square')
            return None
