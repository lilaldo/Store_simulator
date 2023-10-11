from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'André',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': '10 oktober, 2023'
    },
    {
        'author': 'Emma',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': '11 oktober, 2023'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)