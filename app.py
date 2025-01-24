
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/calculate', methods=['POST','GET'])
def calculate():
     
    result = None

    if request.method == 'POST':
        first_number = request.form.get('num1')
        second_number = request.form.get('num2')

        print(first_number, second_number)
        
        result = int(first_number) + int(second_number)

    return render_template('calculate.html', result=result)



if __name__ == '__main__':
    app.run(debug=True)