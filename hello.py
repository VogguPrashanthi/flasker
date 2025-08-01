from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route("/")

# safe - Applies the inline tags to the html
# capitalize 
# lower
# upper
# title - title case
# trim - Removes the trailing spaces
# striptags - Remove any tags that are applied in the html - Helps plain text
# without html tags as it can potentially help hacker inject html through the input

def index():
    first_name = "Prashanthi"
    stuff =  "This is <strong> Bold </strong> Text"

    favorite_pizza = ['Pepperoni', 'Cheese', 'Mushrooms', 41]
    return render_template("index.html", first_name=first_name, stuff=stuff, favorite_pizza=favorite_pizza)

# localhost:5000/user/john
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)


# Create Custome Error Pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error Thing
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

# Running the app
if __name__ == "__main__":
    app.run(debug=True)
