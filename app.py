from flask import Flask, render_template, request

app = Flask(__name__)

# Define a route for the home page


@app.route('/')
def home():
    titles = ['Codepath', 'Devloper Week', 'Grace Hoper Celebration',
              'NSBE', 'OSU Engineering', 'PyCon', 'RTC', 'SWE', 'TAPIA']
    images = ['static/images/codepath.png', 'static/images/devwk.png', 'static/images/GHC.png', 'static/images/nsbe.png',
              'static/images/osu.jpeg', 'static/images/pycon.png', 'static/images/rtc.png', 'static/images/swe.png', 'static/images/tapia.png']
    zipped = zip(titles, images)
    return render_template('index.html', zipped=zipped)


@app.route('/reviews')
def reviews():
    title = request.args.get('title')

    return render_template('reviews.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)
