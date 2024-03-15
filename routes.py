from resources.user import UsersApi, UserApi
from resources.auth import SignupApi, LoginApi

def initialize_routes(api):
    # user
    api.add_resource(UsersApi, '/api/users')
    api.add_resource(UserApi, '/api/users/<id>')

    # auth
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')