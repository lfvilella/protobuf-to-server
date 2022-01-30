import fastapi
import pydantic.error_wrappers
from fastapi import exception_handlers

import github_pydantic
from services import github_service

app = fastapi.FastAPI()


@app.exception_handler(pydantic.error_wrappers.ValidationError)
async def validation_exception_handler(request, exc):
    return await exception_handlers.request_validation_exception_handler(
        request, exc
    )


@app.get("/rest/search", response_model=github_pydantic.GHSearchResponse)
def search(
    q: github_pydantic.GHSearchRequest = fastapi.Depends(
        github_pydantic.GHSearchRequest
    ),
):
    return github_service.search(q)
