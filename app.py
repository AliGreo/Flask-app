
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import redirect, url_for
import csv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)

class Search(db.Model):
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

@app.route('/calculate', methods=['POST','GET'])
def get_info():

    if request.method == 'POST':
        place = request.form.get('place')
        size = request.form.get('size')
        price = float(request.form.get('price'))

        print(place, size, price)

        # new_search = Search(place=place, size=size, pricr=price)

        # try:
        #     db.session.add(new_search)
        #     db.session.commit()
        #     return redirect('/done')
        # except:
        #     return 'There was an issue adding your search'
        with open('data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([place, size, price])



    return render_template('done.html')


@app.route('/done', methods=['POST','GET'])
def done():
    return render_template('done.html')

@app.route('/about', methods=['POST','GET'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)