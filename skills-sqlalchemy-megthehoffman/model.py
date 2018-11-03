"""Models and database functions for cars db."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

# Model definitions

class Human(db.Model):
    """Human model."""

    __tablename__ = "humans"

    human_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    # Create a relationship between Human and Animal via the human_id fkey
    animal = db.relationship("Animal")

    def __repr__ (self):
        """Provide helpful information when printed."""

        return f"""<Human human_id={self.human_id} 
                    fname={self.fname} 
                    lname={self.lname}>"""


class Animal(db.Model):
    """Animal model."""

    __tablename__ = "animals"

    animal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    human_id = db.Column(db.Integer, db.ForeignKey('humans.human_id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    animal_species = db.Column(db.String(25), nullable=False)
    birth_year = db.Column(db.Integer, nullable=True)

    # Create a relationship between Human and Animal via the human_id fkey
    human = db.relationship("Human")

    def __repr__(self):
        """Provide helpful information when printed."""

        return f"""<Animal animal_id={self.animal_id}
                    human_id={self.human_id}
                    name={self.name}
                    animal_species={self.animal_species}
                    birth_year={self.birth_year}>"""

# End Part 1


##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print("Connected to DB.")


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///animals'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    init_app()
