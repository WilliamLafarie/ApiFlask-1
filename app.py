from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {
        'name': 'Bobby',
        'age': 23,
        'job': 'Oui'
    },
    {
        'name': 'Joe',
        'age': 45,
        'job': 'Patron de son propre bar'
    },
    {
        'name': 'Jacky',
        'age': 51,
        'job': 'Président du Fan club de Johnny Halliday'
    },
]


# Get Request
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})


# Get Request with parameters
@app.route('/users/<string:name>', methods=['GET'])
def get_users_by_name(name):
    for user in users:
        if user['name'] == name:
            return jsonify(user)


# Post Request
@app.route('/users', methods=['POST'])
def create_users():
    # Assign Request Data to variable
    request_body = request.get_json()

    # Create New User Dictionary
    new_user = {
        'name': request_body['name'],
        'age': request_body['age'],
        'job': request_body['job']
    }

    # Add New User to ALL User dictionnary
    users.append(new_user)

    # Return data as json
    return jsonify(new_user)


# Put Request
@app.route('/users/<string:name>', methods=['PUT'])
def update_users(name):
    # Assign Request Data to variable
    request_body = request.get_json()

    for user in users:
        if user['name'] == name:
            user['name'] = request_body['name']
            user['age'] = request_body['age']
            user['job'] = request_body['job']
            return jsonify(user)
        else:
            return jsonify({'error': 'No user Found'})


# Delete Request
@app.route('/users/<string:name>', methods=['DELETE'])
def delete_users(name):
    for (index, user) in enumerate(users):
        if user["name"] == name:
            del users[index]
            return jsonify({"message": "User Deleted"})
        else:
            return jsonify({'error': 'No User Found'})


# Server start port
app.run(port=5000)
