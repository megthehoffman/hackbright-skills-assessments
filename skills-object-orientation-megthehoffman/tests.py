"""
>>> import assessment
>>> assessment.road_1.num_lanes
4
>>> assessment.road_2.num_lanes
2
>>> user = assessment.User("Balloonicorn", "sparkles683")
>>> user.update_password("sparks683", "binarysearch47")
Invalid password
>>> user.update_password("sparkles683", "binarysearch47")
>>> user.password
'binarysearch47'
>>> library = assessment.Library()
>>> library.add_book("The Bell Jar", "Sylvia Plath")
>>> library.books[0].title
'The Bell Jar'
>>> books = library.find_books_by_author("Sylvia Plath")
>>> books[0].title
'The Bell Jar'
>>> square = assessment.Square(5)
>>> square.calculate_area()
25.0
>>> square.width = 6
>>> square.calculate_area()
Invalid Square

"""

import doctest
if doctest.testmod().failed == 0:
    print("*** ALL TESTS PASSED ***")
    print()
