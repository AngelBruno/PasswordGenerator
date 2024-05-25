from flask import Flask, render_template  # Importing class Flask

# Initializing the website creating a instance of the Flask class | __name__ == __main__ here
app = Flask(__name__, '/static')

# Indicating to flask what URL should trigger our function
@app.route("/")
def homepage():
    return render_template("homepage.html")

# Putting the website up
if __name__ == '__main__':
    app.run(debug=True)