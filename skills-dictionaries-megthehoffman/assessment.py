"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    # Make an empty dictionary, split the string into a sorted list of words
    dictionary = {}
    words_list = phrase.rstrip().split(' ')
    words_list = sorted(words_list)
    
    # print(words_list)

    # For each word in the list of words, make word the key of the dictionary
    # Set that key equal to dictionary.get, which returns the value for that key
    # Can set the initial value for the key after the comma
    # Then add one each time the word is in the list
    for word in words_list:
        # If we want to remove punctuation and capitalization
            # word = word.lower(),strip(",.!'_[]@#$\"?;:-")
            dictionary[word] = dictionary.get(word, 0) + 1

    return dictionary

 
def print_melon_at_price(price):
    """Given a price, print all melons available at that price, in alphabetical order.

    Here are a list of melon names and prices:

    Honeydew 2.50
    Cantaloupe 2.50
    Watermelon 2.95
    Musk 3.25
    Crenshaw 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If there are no melons at that price print "None found"

        >>> print_melon_at_price(2.50)
        Cantaloupe
        Honeydew

        >>> print_melon_at_price(2.95)
        Watermelon

        >>> print_melon_at_price(5.50)
        None found
    """

    # I think we are supposed to just make an initial dictionary, since we aren't given a .txt?
    # Or maybe move the list into a .txt and open the file in this fcn?
    melon_dict = {'Honeydew': 2.50, 'Cantaloupe': 2.50, 'Watermelon': 2.95, 'Musk': 3.25, \
                    'Crenshaw': 3.25, 'Christmas': 14.25}

    # KEYS
    melon_list = []

    # If the input price is found in the list of values (melon prices), proceed
    # For every melon in the melon_dict, if the melon price == input price, add melon to list
    # Sort the melon list
    if price in melon_dict.values():
        for melon in melon_dict:
            if melon_dict[melon] == price:
                melon_list.append(melon)
                melon_list = sorted(melon_list)
    else:
        print('None found')

    # Print each melon in the melon list
    for melon in melon_list:
        print(melon)


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    # Same thought as above: create a dictionary for use within fcn?
    translation_dict = {'sir': 'matey', 'hotel': 'fleabag inn', 'student': 'swabbie', 'man' :\
                        'matey', 'professor': 'foul blaggart', 'restaurant': 'galley', 'your' :\
                        'yer', 'excuse': 'arr', 'students': 'swabbies', 'are': 'be', 'restroom' :\
                        'head', 'my': 'me', 'is': 'be'}

    # Create a list of pirate words (once translated) to join into returned sentence
    pirate_words = []

    # Split the string of English words into a list of separate words
    english_words = phrase.rstrip().split(' ')
    
    # For each word in the list of English words, determine if that word is in the dictionary
    # Word would be included as a KEY
    # Leave the english_word unchanged if not available in translation_dict
    for english_word in english_words:
        if english_word in translation_dict.keys():
            pirate_word = translation_dict[english_word]
        else:
            pirate_word = english_word
        pirate_words.append(pirate_word)

    # Join string of priate_words into sentence
    return ' '.join(pirate_words)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    # Recall: names is a list
    # Start at names[0]
    
    # Create a list that will hold the returned words
    # Argument names is already in list form
    new_list = []
    names_dict = {}

    
    # Append the first item in the given list to the new_list output, remove it from old list
    # Won't actually work, because then I can't reference the last letter of that word
    # new_list.append(names[0])
    # names.remove(names[0])


    # Store the last letter as a separate value
    # Compare stored value to the index[0] of the rest of the words in the dictionary
    # Make sure keys are not equivalent 
    # While statement, stop when find a word that matches and then start the loop over   
    # Cannot delete a word out of dict mid-iteration, but don't want to use the same word twice
    

    # Make a dictionary whose keys are each name in the list, and whose values are the first
    # and last letter of each word
    for name in names:
        names_dict[name] = (name[0], name[-1])
        # print(names_dict)
    
    for name in names_dict:
        next_letter = names_dict[name][1]
        # print(names_dict[name][1])
        # for keys in names_dict.keys():
        #     if names_dict[name][0] == next_letter:
        #         # print(name)
        #         new_list.append(name)

        # Can work by fluke for third docstring, but is not actually functioning correctly

    # Need to figure out a way to save the last letter of one word, eliminate that word from
    # the dictionary, and then find out what the next word is whose first letter or as written
    # here, name[0], is equivalent to the variable set as next_letter

    # Maybe do reverse? Add all to list and then eliminate if not used?

    return new_list

def kids_game2(names):
    if len(names) == 0:
        return []

    # Setup a dictionary to hold first letters of the names mapped to the index 
    # at which they appear in names list. Since there could be multiple names that
    # start with the same letter, we want the dict values to be lists of indices
    first_letter_dict = {}
    for name_index in range(len(names)):
        name = names[name_index]
        first_letter = name[0]
        if first_letter not in first_letter_dict:
            # This is the first time this letter appeared
            first_letter_dict[first_letter] = [name_index] 
        else:
            # This letter has already appeared before
            first_letter_dict[first_letter].append(name_index)

    print(first_letter_dict)

    final_names = []
    # We know that the first name in the list will have an entry in the dictionary
    # so we'll start with the first letter        
    next_letter = names[0][0]
    # As long as the next_letter has another entry in the dict, we will continue
    # building the final_names list
    while next_letter in first_letter_dict:
        # get the list of indices where this letter appears (note that the
        # indices are ordered based on how we built the dict)
        letter_index_list = first_letter_dict[next_letter]
        # remove and store the next index; we remove it so this name cannot be reused
        index_of_name_to_add = letter_index_list.pop(0)
        # get the name at that index, 
        name_to_add = names[index_of_name_to_add]
        # add the name to our final list
        final_names.append(name_to_add)
        
        # Because we want the while loop to stop when the next_letter no longer
        # exists in the dict, we need to completely remove the key from the dict
        # if there are no more indices left for that letter. Even if the
        # letter_index_list was an empty list, next_letter in first_letter_dict
        # would return true and the while loop would incorrectly keep running.
        if len(letter_index_list) == 0:
            first_letter_dict.pop(next_letter, None)

        # Finally, set the next letter to the last letter of the word we just added.
        next_letter = name_to_add[-1]

    return final_names        









#####################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    # print()
    # import doctest
    # if doctest.testmod().failed == 0:
    #     print("*** ALL TESTS PASSED ***")
    # print()

    result1 = kids_game2(["bagon", "baltoy", "yamask", "starly",
                    "nosepass", "kalob", "nicky", "booger"])
    result2 = kids_game2(["apple", "berry", "cherry"])
    result3 = kids_game2(["noon", "naan", "nun"])

    print(result1)
    print(result2)
    print(result3)
