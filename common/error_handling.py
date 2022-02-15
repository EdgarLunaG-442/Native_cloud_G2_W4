from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class AppErrorBaseClass(Exception):
    pass


class ObjectNotFound(AppErrorBaseClass):
    pass


class NotAllowed(AppErrorBaseClass):
    pass


class NotReady(AppErrorBaseClass):
    pass


def add_custom_errors(app: FastAPI):
    @app.exception_handler(AppErrorBaseClass)
    async def handle_exception_error(request: Request, exc: AppErrorBaseClass):
        return JSONResponse(status_code=500, content={"error": f"Internal server error, error: {exc}"})


    @app.exception_handler(ObjectNotFound)
    async def handle_404_error(request: Request, exc: ObjectNotFound):
        return JSONResponse(status_code=404, content={"error": f"not found error, : {exc}"})

    @app.exception_handler(NotAllowed)
    async def handle_401_error(request: Request, exc: NotAllowed):
        return JSONResponse(status_code=401, content={"error": f"Unauthorized, : {exc}"})

