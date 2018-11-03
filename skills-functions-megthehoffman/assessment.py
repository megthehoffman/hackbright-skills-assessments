"""
Skills function assessment.

Please read the instructions first. Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

#    (a) Write a function that takes a town name as a string and returns
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi, 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.

def is_hometown(town):
    """Determines if a town name is my hometown

    >>> is_hometown("Leola")
    True

    >>> is_hometown("San Leandro")
    False

    """

    if town == "Leola":
        return True
    else:
        return False 

def combine_names(first,last):
    """Concatenates first and last names into one string

    >>> combine_names("Megan","Hoffman")
    'Megan Hoffman'

    """

    full_name = (first + " " + last)
    #Must return, because part c needs it returned, as opposed to printed--hence single quotes around returned value in doctest 
    return full_name


def greets_by_town(town,first,last):
    """Greets a person by name depending on their hometown

    >>> greets_by_town("Leola","Michaela","Horst")
    Hi, Michaela Horst, we're from the same place!

    >>> greets_by_town("Indianola","Zach","Heater")
    Hi, Zach Heater, I'd like to visit Indianola!

    """

    #print(combine_names(first,last))

    if is_hometown(town) == True:
        print("Hi, " + combine_names(first,last) + ", we're from the same place!")
    else:
        print("Hi, " + combine_names(first,last) + ", I'd like to visit " + town + "!")


###############################################################################

# PART TWO

#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry",
#        "blackberry", or "currant."

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.

#    (c) Make a function that takes in a fruit name and a list of fruits. It should
#        return a new list containing the elements of the input list, along with
#        given fruit, which should be at the end of the new list.

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price of $100 or less and $3 for items over $100. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees.


def is_berry(fruit):
    """Determines if fruit is a berry

    >>> is_berry("blackberry")
    True

    >>> is_berry("currant")
    True

    >>> is_berry("durian")
    False

    >>> is_berry("banana")
    False

    """

    if fruit == "strawberry" or fruit == "raspberry" or fruit == "blackberry" or fruit == "currant":
        return True
    else:
        return False


def shipping_cost(fruit):
    """Calculates shipping cost of fruit

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    """

    if is_berry(fruit) == True:
        return 0
    else:
        return 5


def append_to_list(lst, fruit):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list(['banana', 'apple', 'blackberry'], 'dragonfruit')
    ['banana', 'apple', 'blackberry', 'dragonfruit']

    >>> fruits = ['banana', 'apple', 'blackberry']

    >>> append_to_list(fruits, 'dragonfruit')
    ['banana', 'apple', 'blackberry', 'dragonfruit']
    
    >>> fruits
    ['banana', 'apple', 'blackberry']

    """

    #Docstring says with given number added to end? Given fruit? 

    new_lst = lst[:]
    new_lst.append(fruit)

    return new_lst


def calculate_price(base_price,state,tax_percent=0.05):
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

    """

    if state != "CA" and state != "PA" and state != "MA":
        total_price = base_price * (1 + tax_percent)
    if state == "CA":
        prefee_price = base_price * (1 + tax_percent)
        total_price = prefee_price * 1.03
    if state == "PA":
        total_price = (base_price * (1 + tax_percent)) + 2
    if state == "MA":
        prefee_price = base_price * (1 + tax_percent)
        if prefee_price <= 100:
            total_price = prefee_price + 1
        if prefee_price > 100:
            total_price = prefee_price + 3

    return total_price


###############################################################################

# PART THREE

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.

#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.

#        Example:

#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

def makes_list(lst,*items):
    """Takes in a list and any number of addl arguments, adds args to list
    
    >>> makes_list([1, 2, 3, 4], 5,)
    [1, 2, 3, 4, 5]

    >>> makes_list(['a','b'],'c','d','e','f')
    ['a', 'b', 'c', 'd', 'e', 'f']

    >>> makes_list([1, 2, 3, 4], 5, 6)
    [1, 2, 3, 4, 5, 6]
    """

    #Need to make items into a tuple to send in as an argument?
    
    #lst.append(list(items))

    for i in items:
        lst.append(i) 
       
        #Used to make sure fcn was recognizing tuple in arguments
        #print("This fcn took in " + str(len(*items)) + " arguments.")

    return lst

def outer_word_multiplied(word):
    """Takes in a word, for use in innter fcn--not sure I fully understand the question

    >>> outer_word_multiplied('cheese')
    ('cheese', 'cheesecheesecheese')

    >>> outer_word_multiplied('cheddar')
    ('cheddar', 'cheddarcheddarcheddar')

    >>> outer_word_multiplied('mozzarella')
    ('mozzarella', 'mozzarellamozzarellamozzarella')

    """

    def inner_word_multiplied(word):
        #Don't think I need a docstring/doctest for this, since it's a nested fcn
        #Looked up that the point of inner fcns is to keep them out of the global scope

        inner_t = 3 * word 
     
        #Trying regular math operations to see if you can multiply strings
        #created_tuple[1] = 2 * word

        return inner_t

    created_tuple = (word, inner_word_multiplied(word))
    
    print(created_tuple)



###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()
