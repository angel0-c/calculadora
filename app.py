from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        expression = request.json['expression']
        result = eval(expression)  # Evaluamos la expresión matemática recibida
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
