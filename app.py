from flask import Flask

app =Flask(__name__)
@app.route('/froyo')
def choose_froyo():
    context = {
        'users_flavor': request.arg.get('flavor')
        'users_toppings': request.arg.get('toppings')
    }

    return render_template('index.html',**context)

    
@app.route('/froyo_results')
def show_froyo_results():
    
    return render_template('froyo.html')
   
@app.route('/favorites')
def choose_favorites():
    """Shows a form to collect users favorite color, animal, and city."""
    return """
    <form action="/favorite_results" method="GET">
        What is your favorite color?<br>
        <input type="text" name="color">
        </br>
        What is ypur favorite animal?<br>
        <input type="text" name="animal">
        </br>
        What is your favorite city?
        <input type="text" name="city">
        </br>
        <input type="submit" value="Submit">
    </forms> """

@app.route('/favorite_results')
def show_favorite_results():
    users_color = request.args.get('color')
    users_animal = request.args.get('animals')
    users_city = request.args.get('city')
    return f"Wow, I didn't know {users_color} {users_animal} lived in {users_city}!"

@app.route('/secret_message')
def secret_message():
    return """
    <form action="/message_results" method="POST">
        Enter your secret message<br>
        <input type="text" name="message">
        </br>
        <input type="submit" value="Submit">
    </forms> """

@app.route('/message_results')
def show_message():
    users_message = request.forms.get('message')
    message_abc = .sort_letters(users_message) 
    return f"Here's your secret message {message_abc}" 

if __name__ == '__main__':
    app.run(debug=True)
