
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import redirect, url_for
import csv
import os
import pandas as pd

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)

class Search(db.Model):
    user_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(100), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Search('{self.id}')"


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/done', methods=['POST','GET'])
def done():

    if request.method == 'POST':
        user_name = request.form.get('username')
        phone_number = request.form.get('phone_number')
        place = int(request.form.get('place'))
        size = float(request.form.get('size'))
        price = float(request.form.get('price'))


        with open('data.csv', mode='a') as file:
            writer = csv.writer(file)
            writer.writerow([user_name, phone_number,place, size, price])

        data = pd.read_csv('data.csv').to_dict(orient='records')

        return redirect(url_for('done', data=data))
    
    else:
        return redirect(url_for('done'))

@app.route('/about', methods=['POST','GET'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)