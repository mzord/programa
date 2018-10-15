from flask import Flask, render_template
import forms

app = Flask(__name__)

@app.route('/')
def helloworld():
    return "Hello World"


@app.route('/teste', methods=['GET'])
def hello():
    form = MyForm()
    return render_template('index.html')

if __name__ = '__main__'
    app.run()