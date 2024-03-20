from flask import Flask

app = Flask(__name__)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    return f"Result of addition: {result}"

@app.route('/sub/<int:num1>/<int:num2>')
def subtract(num1, num2):
    result = num1 - num2
    return f"Result of subtraction: {result}"

@app.route('/mult/<int:num1>/<int:num2>')
def multiply(num1, num2):
    result = num1 * num2
    return f"Result of multiplication: {result}"

@app.route('/div/<int:num1>/<int:num2>')
def divide(num1, num2):
    if num2 != 0:
        result = num1 / num2
        return f"Result of division: {result}"
    else:
        return "Cannot divide by zero!"
    
@app.route('/')
def hello():
    return "hello world"

if __name__ == '__main__':
    app.run(debug=True, port=8080)
