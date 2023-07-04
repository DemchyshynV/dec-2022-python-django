from rest_framework.response import Response
from rest_framework.views import exception_handler

from core.enums.error_enum import ErrorEnum
from core.exceptions.jwt_exception import JwtException


def error_handler(exc: Exception, context: dict) -> Response:
    handlers = {
        'JwtException': _jwt_validation_error
    }

    response = exception_handler(exc, context)
    exc_class = exc.__class__.__name__

    if exc_class in handlers:
        return handlers[exc_class](exc, context)

    return response


def _jwt_validation_error(exc: JwtException, context: dict) -> Response:
    return Response(ErrorEnum.JWT.msg, ErrorEnum.JWT.code)
