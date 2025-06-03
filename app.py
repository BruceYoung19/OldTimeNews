from flask import Flask,render_template,request
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    today = date.today()
    return render_template('main.html', today_date=today)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    subject = request.form['search_subject']
    print(subject)
    return "result"

if __name__ == '__main__':
    app.run(debug=True)
