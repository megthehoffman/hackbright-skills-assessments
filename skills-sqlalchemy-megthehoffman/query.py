"""

This file is the place to write solutions for parts two and three of skills-
sqlalchemy. Remember to consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you here, so refer to classes
by just their class name (not model.ClassName).

"""

from model import *

init_app()

# -----------------
# PART TWO: QUERIES
# -----------------

# Could, but don't need to query with db.session because we only have one session

# Get the human with the id 2.
q1 = Human.query.filter_by(human_id=2).one()
# Checked via comparison of psql animals/running model

# Get the *first* animal with the species 'fish'
q2 = Animal.query.filter_by(animal_species='fish').first()
# Checked via comparison of psql animals/running model

# Get all of the animals for the human with the id 5 and the animal species 'dog'
q3 = Animal.query.filter_by(human_id=5, animal_species='dog').all()
# Checked via comparison of psql animals/running model

# Get all the animals that were born after 2015 (do not include animals without birth years).
q4 = Animal.query.filter(Animal.birth_year > 2015).all()
# Checked via comparison of psql animals/running model

# Find the humans with first names that start with 'J'
q5 = Human.query.filter(Human.fname.like('J%')).all()
# Checked via comparison of psql animals/running model

# Find all the animals without birth years in the database.
q6 = Animal.query.filter(Animal.birth_year == None).all()
# Checked via comparison of psql animals/running model

# Find all animals that are either fish or rabbits
q7 = Animal.query.filter((Animal.animal_species=='fish')|(Animal.animal_species=='rabbit')).all()
# Checked via comparison of psql animals/running model

# Find all the humans whose email addresses do not contain 'gmail'
q8 = Human.query.filter(Human.email.notlike('%gmail%')).all()
# Checked via comparison of psql animals/running model


# ---------------------
# PART THREE: FUNCTIONS
# ---------------------

# ***Do not use more than one query for each function***

# 1. Write a function, print_directory, which does not take any arguments
#    and prints out each human (once) with a list of their animals.

#    The output should look like this (with tabs to indent each animal name under
#    a human's name)

#       Human_first_name Human_last_name
#           Animal name (animal species)
#           Animal name (animal species)
#
#       Human_first_name Human_last_name
#           Animal name (animal species)

def print_directory():
    """Prints out each human (once) with a list of their animals."""

    # Attempted to group by human_id
    # Group by works only for base tables, per the Internet/can't collapse certain data

    result = db.session.query(Animal.name, Animal.animal_species, Human.fname, 
                Human.lname, Human.human_id).join(Human).order_by(Human.human_id).all()

    current_id = None
    for name, animal_species, fname, lname, human_id in result:
        if current_id != human_id:
            print(fname, lname)
            current_id = human_id

        print('\t' + name + '(' + animal_species + ')')
   

# 2. Write a function, get_animals_by_name, which takes in a string representing
#    an animal name (or part of an animal name) and *returns a list* of Animal
#    objects whose names contain that string.

def get_animals_by_name(name):
    """Takes a string representing any part of an animal name and returns a list
    of animal objects whose names contain that string."""

    result = Animal.query.filter(Animal.name.like('%'+name+'%')).all()
    # print(result)

    return result

# 3. Write a function, find_humans_by_animal_species, which takes in an animal
#    species and *returns a list* of all of Human objects who have animals of
#    that species.

def find_humans_by_animal_species(species):
    """Takes in an animal species and returns a list of all Human objects who 
    have animals of that species."""

    result = db.session.query(Human).join(Animal).filter(Animal.animal_species==species).all()
    # print(result)
    
    return result 


print_directory()
# get_animals_by_name('nk')
# get_animals_by_name('i')
# print(get_animals_by_name('ff'))
# get_animals_by_name('id')
# get_animals_by_name('e')
# find_humans_by_animal_species('cat')
# find_humans_by_animal_species('dog')
