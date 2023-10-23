from flask import Flask, render_template
from backend.routes.reviews import reviews_bp
from backend.routes.reviews import populate_db
import backend.routes.reviews

app = Flask(__name__)


# Define a route for the home page


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/fair')
def fair():
    return render_template('fair.html')


@app.route('/reviews')
def reviews():
    data = backend.routes.reviews.get_all_reviews().get_json()
    return render_template('reviews.html', data=data)


if __name__ == '__main__':
    app.register_blueprint(reviews_bp)
    populate_db()
    app.run(debug=True)
