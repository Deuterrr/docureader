from fastapi.responses import JSONResponse


class APIResponse:
    @staticmethod
    def success(data=None, message="success"):
        if not data:
            return JSONResponse(status_code=200, content={
                "code": "002",
                "message": "success with empty data",
                "data": []
            })
        return JSONResponse(status_code=200, content={
            "code": "000",
            "message": message,
            "data": data
        })


    @staticmethod
    def invalid_input(message="invalid input"):
        return JSONResponse(status_code=400, content={
            "code": "003",
            "message": message,
            "data": []
        })


    @staticmethod
    def data_not_found(message="data not found"):
        return JSONResponse(status_code=404, content={
            "code": "004",
            "message": message,
            "data": []
        })


    @staticmethod
    def error_process(message="error process"):
        return JSONResponse(status_code=500, content={
            "code": "001",
            "message": message,
            "data": []
        })


    @staticmethod
    def internal_error(message="internal error"):
        return JSONResponse(status_code=500, content={
            "code": "005",
            "message": message,
            "data": []
        })
