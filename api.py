from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='My API',
          description='Hi hi, looks like you are good one, lets see how you will pass your next challenge. Now you '
                      'see a little confusing API. You should make three requests in correct order and get уцтскнзеув '
                      'еуче')

# Define the request and response models for the Login endpoint
login_request = api.model('LoginRequest', {
    'username': fields.String(required=True),
    'password': fields.String(required=True)
})

login_response = api.model('LoginResponse', {
    'token': fields.String
})


@api.route('/login')
class Login(Resource):
    @api.expect(login_request)
    @api.response(200, 'Success', login_response)
    def post(self):
        # Get the username and password from the request
        username = request.json['username']
        password = request.json['password']

        # Check if the username and password match the defined credentials
        if username == 'superpuperqa' and password == 'devsucks':
            # Return a token if the credentials are correct
            return {'token': 'awesome_admin_token'}, 200
        else:
            # Return an error message if the credentials are incorrect
            return {'message': 'Invalid credentials'}, 401


# Define the request and response models for the Text endpoint
text_response = api.model('TextResponse', {
    'text': fields.String
})


@api.route('/post')
class Post(Resource):
    @api.doc(security='apiKey')
    @api.header('Authorization', 'Admin token', required=True)
    @api.response(200, 'Success', text_response)
    def get(self):
        # Get the authorization header from the request
        header = request.headers.get('Authorization')

        # Check if the authorization header matches the defined token
        if header == 'awesome_admin_token':
            # Return the text if the token is correct
            return {'text': 'please, continue, you need parameter: bmw_better_audi'}, 200
        else:
            # Return an error message if the token is incorrect
            return {'message': 'Unauthorized'}, 401


# Define the request and response models for the Check endpoint
check_request = api.model('CheckRequest', {
    'parameter': fields.String(required=True)
})

check_response = api.model('CheckResponse', {
    'message': fields.String
})


@api.route('/get')
class Get(Resource):
    @api.doc(security='apiKey')
    @api.expect(check_request)
    @api.header('Authorization', 'Admin token', required=True)
    @api.response(200, 'Success', check_response)
    def post(self):
        # Get the parameter from the request
        parameter = request.json['parameter']

        # Check if the parameter equals the text defined in the class
        if parameter == 'bmw_better_audi':
            # Return a message if the parameter is equal to the text
            return {'message': 'Very Good, this cyphered text: dpdclqj_pb_brxqj_kdfnhuv'}, 200
        else:
            # Return an error message if the parameter is not equal to the text
            return {'message': 'Incorrect parameter'}, 400


@api.route('/help')
class Get(Resource):
    @api.doc(security='apiKey')
    @api.header('Authorization', 'Admin token', required=True)
    @api.response(200, 'Success', text_response)
    def get(self):
        # Get the authorization header from the request
        header = request.headers.get('Authorization')

        # Check if the authorization header matches the defined token
        if header == 'awesome_admin_token':
            # Return the text if the token is correct
            return {'text': 'Краще бути першим у селі, ніж другим у Римі'}, 200
        else:
            # Return an error message if the token is incorrect
            return {'message': 'Unauthorized'}, 401


if __name__ == '__main__':
    app.run(debug=True)
