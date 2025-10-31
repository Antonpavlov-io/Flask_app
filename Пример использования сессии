from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/example')
def example():
    session['example'] = 'example_value'
    return session['example']

if __name__ == '__main__':
    app.run(debug=True)
