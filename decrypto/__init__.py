from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('base.html')


@app.route("/submit", methods=['POST', 'GET'])
def submit():

    if request.method == 'GET':
        user = request.args.get('cipher')
        print(user)
    return ("Hello world")


if __name__ == '__main__':
    app.run(debug=True)
