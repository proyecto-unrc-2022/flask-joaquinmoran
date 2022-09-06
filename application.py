from flask import Flask, jsonify, request, Response

app = Flask(__name__)

USERS = {}

@app.route('/')
def index():
    return 'Index Page'

@app.route("/users/<username>", methods=['GET'])
def access_users(username):
    if request.method == 'GET':
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return Response(status=404)

#Second scenario----------------------------------------------------------------------------------

@app.route("/users/logguser", methods=['POST'])
def new_user():
    if request.method == 'POST':
        USERS.update(johnl=request.json['johnl'])
        newuser = USERS.get('johnl')
        return jsonify(newuser)
    else:
        return Response(status=404)

#Third scenario----------------------------------------------------------------------------------  

@app.route("/users/updateuser", methods=['PUT'])
def update_user():
    if request.method == 'PUT':
        USERS.update(paulm=request.json['paulm'])
        updated_user = USERS.get('paulm')
        return jsonify(updated_user)
    else:
        return Response(status=404)

#Fourth scenario-----------------------------------------------------------------------------------

@app.route("/users/delete/<deleteuser>", methods=['DELETE'])
def delete_user(deleteuser):
    if request.method == 'DELETE':
        user = USERS.get(deleteuser)
        deleted_user=USERS.pop(deleteuser,'error')
        if deleted_user == user:
            return jsonify(user)
        else:
            return Response(status=404)
    else:
        return Response(status=404)  

#Fifth scenario-------------------------------------------------------------------------------------
@app.route("/users/all/<allusers>", methods=['GET'])
def all_users(allusers):
    if request.method == 'GET':
        return jsonify(allusers)
    else:
        return Response(status=404)

if __name__ == "__main__":
    app.run()
