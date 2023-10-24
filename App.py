import os
from flask import Flask, render_template, send_from_directory, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Rudraprasad%40123@localhost/lms'
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)


class books(db.Model):
    SERIAL_NO = db.Column(db.Integer, primary_key=True)
    BOOK_NAME = db.Column(db.String(50))
    AUTHOR_NAME = db.Column(db.String(50))
    RATING = db.Column(db.Integer)
    Borrower_ID = db.Column(db.Integer)

    def __init__(self, BOOK_NAME, AUTHOR_NAME, RATING, Borrower_ID):
        # self.SERIAL_NO = SERIAL_NO
        self.BOOK_NAME = BOOK_NAME
        self.AUTHOR_NAME = AUTHOR_NAME
        self.RATING = RATING
        self.Borrower_ID = Borrower_ID


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/x-icon')


@app.route('/insert', methods=['POST'])
def insert():

    if request.method == 'POST':
        BOOK_NAME = request.form['BOOK_NAME']
        AUTHOR_NAME = request.form['AUTHOR_NAME']
        RATING = request.form['RATING']
        Borrower_ID = request.form['Borrower_ID']

        my_data = books(BOOK_NAME,AUTHOR_NAME,RATING,Borrower_ID)
        
        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
