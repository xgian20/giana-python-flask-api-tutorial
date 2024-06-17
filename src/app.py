from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {
        "label": "Wash car",
        "done": False 
    },
    {
        "label": "Do homework",
        "done": False
    }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)



















if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)



