from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/car_choose')
def about():
    return render_template("car_choose.html")


@app.route('/rent')
def rent():
    return render_template("rent.html")


if __name__ == "__main__":
    app.run(port=4565, debug=False)
