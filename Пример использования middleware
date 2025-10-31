from flask import Flask, request

app = Flask(__name__)

@app.before_request
def before_request():
    print('Before request')

@app.after_request
def after_request(response):
    print('After request')
    return response

@app.route('/example')
def example():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
