from flask import jsonify
from werkzeug.exceptions import HTTPException

def register_jwt_handlers(app, jwt):
    print("Estou sendo chamado aqui")

    @jwt.invalid_token_loader
    def invalid_token_callback(reason):
        '''Invalid token handler'''
        return jsonify({
            "error": "Invalid Token!",
            "message": reason
        }), 401
    
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        '''Expired token handler'''
        return jsonify({
            "error": "Expired Token!",
            "message": "Please, log in again..."
        }), 401

    @jwt.unauthorized_loader
    def unauthorized_callback(reason):
        '''No token handler'''
        return jsonify({
            "error": "Authorization token required",
            "message": reason
        }), 401
    
    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        '''HTTP Exceptions handler'''
        return jsonify({
            "error": "Erro de solicitação.",
            "message": error.description
        }), error.code