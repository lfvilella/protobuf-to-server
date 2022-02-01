import github_pydantic


def search(
    request: github_pydantic.GHSearchRequest,
    serving_backend: str,
) -> github_pydantic.GHSearchResponse:
    return github_pydantic.GHSearchResponse(
        type=request.type,
        server_response=f"Reponding from {serving_backend} service",
    )
