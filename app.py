from flask import Flask, request, jsonify

app = Flask(__name__)

# CMS content store
contents = []

# CREATE content
@app.route('/contents', methods=['POST'])
def create_content():
    content = request.json
    contents.append(content)
    return jsonify({
        "message": "Content created successfully",
        "content": content
    }), 201

# READ all contents
@app.route('/contents', methods=['GET'])
def get_all_contents():
    return jsonify(contents), 200

# READ content by ID
@app.route('/contents/<int:content_id>', methods=['GET'])
def get_content(content_id):
    for content in contents:
        if content["id"] == content_id:
            return jsonify(content), 200
    return jsonify({"error": "Content not found"}), 404

# UPDATE content
@app.route('/contents/<int:content_id>', methods=['PUT'])
def update_content(content_id):
    updated_data = request.json
    for content in contents:
        if content["id"] == content_id:
            content.update(updated_data)
            return jsonify({
                "message": "Content updated successfully",
                "content": content
            }), 200
    return jsonify({"error": "Content not found"}), 404

# DELETE content
@app.route('/contents/<int:content_id>', methods=['DELETE'])
def delete_content(content_id):
    global contents
    contents = [c for c in contents if c["id"] != content_id]
    return jsonify({"message": "Content deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
