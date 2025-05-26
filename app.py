from flask import Flask,render_template
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    today = date.today()
    return render_template('main.html', today_date=today)

app.route('/search')
def search():
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
