class APIError(Exception):
    status_code=500
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.message=message
        if status_code is not None:
            self.status_code=status_code

class BadRequestError(APIError):
    status_code=400

class UnauthorizedError(APIError):
    status_code=401

class ForbiddenError(APIError):
    status_code=403

class NotFoundError(APIError):
    status_code=404