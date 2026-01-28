from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory customer database
customers = []

# CREATE customer
@app.route('/customers', methods=['POST'])
def create_customer():
    customer = request.json
    customers.append(customer)
    return jsonify({
        "message": "Customer added successfully",
        "customer": customer
    }), 201

# READ all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(customers), 200

# READ customer by ID
@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    for customer in customers:
        if customer["id"] == customer_id:
            return jsonify(customer), 200
    return jsonify({"error": "Customer not found"}), 404

# UPDATE customer
@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    updated_data = request.json
    for customer in customers:
        if customer["id"] == customer_id:
            customer.update(updated_data)
            return jsonify({
                "message": "Customer updated successfully",
                "customer": customer
            }), 200
    return jsonify({"error": "Customer not found"}), 404

# DELETE customer
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    global customers
    customers = [c for c in customers if c["id"] != customer_id]
    return jsonify({"message": "Customer deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
