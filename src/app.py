from flask import Flask, jsonify, request

app = Flask(__name__)

# 1. Variable global todos declarada fuera de cualquier función
# 2. Debe ser una lista
# 3. Con al menos un elemento dummy con el formato requerido
# 4. Cada elemento debe ser un diccionario con las claves "label" y "done"
# 5. El valor de "label" debe ser string
# 6. El valor de "done" debe ser boolean
todos = [
    { "label": "Sample", "done": True }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# 7. Función add_new_todo debe estar declarada
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    
    # Validar que el request tenga el formato correcto
    if not isinstance(request_body, dict):
        return jsonify({"error": "Invalid data format"}), 400
    
    if "label" not in request_body or "done" not in request_body:
        return jsonify({"error": "Missing required fields"}), 400
    
    if not isinstance(request_body["label"], str) or not isinstance(request_body["done"], bool):
        return jsonify({"error": "Invalid field types"}), 400
    
    todos.append(request_body)
    return jsonify(todos)

# 8. Función delete_todo debe estar declarada
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Invalid position"}), 404
    
    del todos[position]
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)