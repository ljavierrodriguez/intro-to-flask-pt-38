from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'


@app.route('/')
def main():
    response = { 
        "status": 200,
        "msg": "Hola Mundo!"
    }
    return jsonify(response)


@app.route('/api/users', methods=['GET'])
def list_users():
    return jsonify([])

@app.route('/api/users', methods=['POST'])
def create_user():
    return jsonify([])

@app.route('/api/users', methods=['GET', 'PUT', 'DELETE'])
def users():
    if request.method == 'GET':
        pass
    
    if request.method == 'PUT':
        pass
    
    if request.method == 'DELETE':
        pass
    

@app.route('/saludo/<name>/<surname>', methods=['GET'])
def saludo_get(name, surname):
    return jsonify({"name": name, "surname": surname})

@app.route('/saludo', methods=['POST'])
def saludo_post():
    
    # JSON Format
    #body = request.get_json() # dict
    
    # name = request.json.get("name")
    # surname = request.json.get("surname")

    #name = body["name"]
    #surname = body["surname"]
    
    # Form Format
    
    name = request.form["name"]
    surname = request.form["surname"]
    
    
    
    return jsonify({"name": name, "surname": surname})


# CRUD = CREATE, READ, UPDATE, DELETE
# METHOD = POST, GET, PUT, DELETE

if __name__ == '__main__':
    app.run()