from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "availability": True},
    {"id": 2, "name": "Chair", "category": "Furniture", "availability": False}
]

# READ
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = next((p for p in products if p["id"] == id), None)
    return jsonify(product) if product else ("Product not found", 404)

# UPDATE
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    product = next((p for p in products if p["id"] == id), None)
    if product:
        product.update(data)
        return jsonify(product)
    return "Product not found", 404

# DELETE
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    global products
    products = [p for p in products if p["id"] != id]
    return '', 204

# LIST ALL / LIST BY NAME / LIST BY CATEGORY / LIST BY AVAILABILITY
@app.route('/products', methods=['GET'])
def list_products():
    category = request.args.get('category')
    name = request.args.get('name')
    availability = request.args.get('availability')

    filtered_products = products
    if category:
        filtered_products = [p for p in filtered_products if p["category"] == category]
    if name:
        filtered_products = [p for p in filtered_products if p["name"] == name]
    if availability:
        filtered_products = [p for p in filtered_products if str(p["availability"]).lower() == availability.lower()]

    return jsonify(filtered_products)
 
