from dataclasses import dataclass
from typing import Any, Optional
import logging

logger = logging.getLogger("app.errors")

@dataclass
class ApiError(Exception):
    message: str
    status_code: int = 400
    type: str = "api_error"
    details: Optional[Any] = None

    @staticmethod
    def not_found(msg: str):
        return ApiError(message=msg, status_code=404, type="not_found")

    @staticmethod
    def bad_request(msg: str, details: Any = None):
        return ApiError(message=msg, status_code=400, type="bad_request", details=details)

    @staticmethod
    def internal(msg: str = "Internal server error", details: Any = None):
        return ApiError(message=msg, status_code=500, type="internal_error", details=details)

    @staticmethod
    def validation(msg: str, details: Any = None):
        return ApiError(message=msg, status_code=422, type="validation_error", details=details)


def api_error_response(error: ApiError):
    return {
        "error": {
            "code": error.status_code,
            "type": error.type,
            "message": error.message,
            "details": error.details,
        }
    }