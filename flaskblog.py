from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app.config['SECRET_KEY'] = '4f2db1d7d91fab2faca964eeaf4e7fb4'
app = Flask(__name__)

# list of dictionaries
posts = [
    {
        'author' : 'Olivia Grey',
        'title' : 'How to live longer',
        'content' : 'First post content',
        'date_posted' : 'April 20, 1999'
    },
    {
        'author' : 'Mike April',
        'title' : 'All about Python',
        'content' : 'Educational post',
        'date_posted' : 'January 1, 2016'
    }
]

@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)