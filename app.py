from flask import Flask,render_templates

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('main.html')

if __name__ = '__main__':
    app.run(debug=True)
