from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    a = request.args.get('a')
    b = request.args.get('b')
    try:
        result = int(a) + int(b)
        return jsonify({"result": result})
    except:
        return jsonify({"error": "Invalid input. Please provide valid numbers."}), 400

@app.route('/subtract', methods=['GET'])
def subtract():
    a = request.args.get('a')
    b = request.args.get('b')
    try:
        result = int(a) - int(b)
        return jsonify({"result": result})
    except:
        return jsonify({"error": "Invalid input. Please provide valid numbers."}), 400

@app.route('/multiply', methods=['GET'])
def multiply():
    a = request.args.get('a')
    b = request.args.get('b')
    try:
        result = int(a) * int(b)
        return jsonify({"result": result})
    except:
        return jsonify({"error": "Invalid input. Please provide valid numbers."}), 400

@app.route('/divide', methods=['GET'])
def divide():
    a = request.args.get('a')
    b = request.args.get('b')
    try:
        if int(b) == 0:
            return jsonify({"error": "Cannot divide by zero"}), 400
        result = int(a) / int(b)
        return jsonify({"result": result})
    except ZeroDivisionError:
        return jsonify({"error": "Cannot divide by zero"}), 400
    except:
        return jsonify({"error": "Invalid input. Please provide valid numbers."}), 400

# Optional: Add a home route
@app.route('/')
def home():
    return '''
    <h1>Calculator API</h1>
    <p>Available endpoints:</p>
    <ul>
        <li>/add?a=number&b=number</li>
        <li>/subtract?a=number&b=number</li>
        <li>/multiply?a=number&b=number</li>
        <li>/divide?a=number&b=number</li>
    </ul>
    '''

if __name__ == '__main__':
    app.run(debug=True)