from flask import jsonify, current_app
from exceptions.api_exceptions import APIError

def register_error_handlers(app):
    @app.errorhandler(APIError)
    def handle_api_error(error):
        return jsonify({"error": error.message}), error.status_code
    
    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        if current_app.debug:
            raise error
        return jsonify({"error": "An unexpected server error occurred."}), 500