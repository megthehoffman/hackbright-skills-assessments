from flask import Flask, redirect, request, render_template, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Getting our list of MOST LOVED MELONS
MOST_LOVED_MELONS = {
    'cren': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg',
        'name': 'Crenshaw',
        'num_loves': 584,
    },
    'jubi': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg',
        'name': 'Jubilee Watermelon',
        'num_loves': 601,
    },
    'sugb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg',
        'name': 'Sugar Baby Watermelon',
        'num_loves': 587,
    },
    'texb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg',
        'name': 'Texas Golden Watermelon',
        'num_loves': 598,
    },
}

# YOUR ROUTES GO HERE

# Do routes require fcn definitions?

@app.route('/')
def user_homepage():
    if 'name' not in session:
        return render_template('homepage.html')
    else:
        return redirect('/top-melons')

@app.route('/top-melons')
def top_melons():

    if 'name' not in session:
        return redirect('/')
    else: 
        return render_template('top-melons.html', MOST_LOVED_MELONS=MOST_LOVED_MELONS)

    # NOTES ON ATTEMPTED SOLUTIONS: 
    
    # for key,value in MOST_LOVED_MELONS.items():

    #     # print(key) 
    #         # Is printing out the keys (melon abbreviations) in the larger dict
    #     # print(value) 
    #         # Is printing out the nested dicts (values of melon abbreviations)
    #     # print(MOST_LOVED_MELONS[key]) 
    #         # Is printing out the values (another dict) for each melon      
    #     # print(MOST_LOVED_MELONS[key]['name']) 
    #         # Is printing out the name in the nested dict


    # Current problem is that the values being passed into the template seem to only be
    # the last values, for the last melon in the dictionary--need to figure out how to
    # pass each melon

    # Can only render the template once, so maybe make each attribute a list to loop 
    # through? Not very concise or efficient 

@app.route('/get-name')
def get_name():

    session['name']=request.args.get('person_name')
    # flash("Thanks! We can check out the rest of the site now.")
    # I think a flash message is necessary for sessions to be saved, but it doesn't appear
    # to actually be doing anything
    print(session)

    return redirect('/top-melons')

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = False

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
