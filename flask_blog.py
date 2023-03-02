from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
    {
        'author': 'Roman Gabriel',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 20, 2021'
    },

    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 21, 2021'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')



if __name__ == '__main__': #only true if the script is runned directly (it is not imported)
    app.run(debug=True) #done this so you don't have to 'flask run' for every code change
