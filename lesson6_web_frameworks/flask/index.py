from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # return "Hello from Flask"
    return render_template('index.html', username="John")

@app.route('/about')
def about():
    # return "Lesson: start work with Flask"
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)