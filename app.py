from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    context = {
        "users_flavor": request.args.get("flavor"),
        "users_toppings": request.args.get("toppings")
    }
    return render_template("froyo_form.html", **context)

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    context = {
        "users_flavor": request.args.get("flavor"),
        "users_toppings": request.args.get("toppings")
    }
    return render_template("froyo_results.html", **context)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorite_results" method="GET">
        What is your favorite color? <br/>
        <input type="text" name="color"><br/>
        What is your favorite animal? <br/>
        <input type="text" name="animal"><br/>
        What is your favorite city? <br/>
        <input type="text" name="city">
        <input type="submit" value="Submit">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    user_color = request.args.get("color")
    user_animal = request.args.get("animal")
    user_city = request.args.get("city")
    return f"Wow, I didn't know {user_color} {user_animal} lived in {user_city}!"

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        What's your secret message?</br>
        <input type="text" name="message">
        <input type="submit" value="Submit">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    user_message = request.form.get("message")
    user_message = sort_letters(user_message)
    return f"Here is your secret message! {user_message}"

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    context = {
        "numberOne": request.args.get("operand1"),
        "numberTwo": request.args.get("operand2"),
        "math0peration": request.args.get("operation")
    }
    return render_template("calculator_form.html", **context)

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    


# List of compliments to be used in the `compliments_results` route (feel free 
# to add your own!) 
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    numCompliments = request.args.get("num_compliments")
    limitedList = random.sample(list_of_compliments, k=int(numCompliments))
    context = {
        # TODO: Enter your context variables here.
        "list_of_compliments": limitedList,
        "users_name": request.args.get("users_name"),
        "wants_compliments": request.args.get("wants_compliments")
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run()
