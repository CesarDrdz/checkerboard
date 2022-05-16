from distutils.log import debug
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<int:number')

def hello_world(number):
    return render_template('index.html', number = number)

if __name__=="__main__":
    app.run(debug=True)