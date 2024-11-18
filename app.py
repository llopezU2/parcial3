from flask import Flask, request, jsonify, render_template
from derivada import calcular_derivada

app = Flask(__name__)

# Valores predefinidos
valores_predefinidos = {
    'xi-2': {'x': 0, 'f(x)': 1.2},
    'xi-1': {'x': 0.25, 'f(x)': 0.1035},
    'xi': {'x': 0.5, 'f(x)': 0.925},
    'xi+1': {'x': 0.75, 'f(x)': 0.6363},
    'xi+2': {'x': 1, 'f(x)': 0.2}
}

@app.route('/')
def home():
    # Renderiza la página HTML
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        h = data['h']
        formula = data['formula']
        result = calcular_derivada(formula, h, valores_predefinidos)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
