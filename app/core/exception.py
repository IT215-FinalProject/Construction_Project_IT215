from fastapi import Request
from fastapi.responses import JSONResponse

# Lỗi khi không tìm thấy dữ liệu
class NotFoundException(Exception):
    def __init__(self, message: str):
        self.message = message

# Lỗi khi dữ liệu không hợp lệ
class BadRequestException(Exception):
    def __init__(self, message: str):
        self.message = message

# Xử lý lỗi 404
async def not_found_handler(
    request: Request,
    exc: NotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "status_code": 404,
            "message": exc.message,
            "data": None,
            "error": "NOT_FOUND"
        }
    )

# Xử lý lỗi 400
async def bad_request_handler(
    request: Request,
    exc: BadRequestException
):
    return JSONResponse(
        status_code=400,
        content={
            "status_code": 400,
            "message": exc.message,
            "data": None,
            "error": "BAD_REQUEST"
        }
    )