import os

from flask import (
    Flask,
    render_template,
    request
)


# Create the application instance
app = Flask(__name__)


@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """

    print("here in home function")

    return render_template('home.html')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()