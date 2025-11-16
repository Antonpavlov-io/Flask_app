from flask import Flask, request

app = Flask(__name__)

@app.route('/example', methods=['GET', 'POST'])
def example():
    if request.method == 'GET':
        return 'GET request'
    elif request.method == 'POST':
        return 'POST request'

if __name__ == '__main__':
    app.run(debug=True)
