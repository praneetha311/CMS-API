from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

customers = []

@app.route('/')
def home():
    return render_template('index.html')

# CREATE
@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.json
    customers.append({
        "id": data["id"],
        "name": data["name"],
        "email": data["email"],
        "phone": data["phone"],
        "city": data["city"]
    })
    return jsonify({"message": "Customer created"}), 201

# READ ALL
@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(customers)

# READ BY ID
@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    for c in customers:
        if c["id"] == customer_id:
            return jsonify(c)
    return jsonify({"error": "Customer not found"}), 404

# UPDATE
@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.json
    for c in customers:
        if c["id"] == customer_id:
            c["name"] = data["name"]
            c["email"] = data["email"]
            c["phone"] = data["phone"]
            c["city"] = data["city"]
            return jsonify({"message": "Customer updated"})
    return jsonify({"error": "Customer not found"}), 404

# DELETE
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    global customers
    customers = [c for c in customers if c["id"] != customer_id]
    return jsonify({"message": "Customer deleted"})

if __name__ == "__main__":
    app.run(debug=True)
