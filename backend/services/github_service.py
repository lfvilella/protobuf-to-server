import github_pydantic


def search(
    request: github_pydantic.GHSearchRequest,
) -> github_pydantic.GHSearchResponse:
    return github_pydantic.GHSearchResponse(
        type=request.type,
        server_response="Reponding from the server",
    )
