from flask import Flask, render_template

app = Flask(__name__)

@app.route('/example')
def example():
    name = 'John'
    age = 30
    return render_template('example.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)
