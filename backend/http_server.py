import fastapi
import github_graphene
import github_pydantic
import graphene
import pydantic.error_wrappers
import starlette_graphene3
from fastapi import exception_handlers
from services import github_service

app = fastapi.FastAPI(
    docs_url="/rest/docs",
    openapi_url="/rest/openapi.json",
)


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
    return github_service.search(q, "REST API")


class Query(graphene.ObjectType):
    search = graphene.Field(
        github_graphene.GHSearchResponse,
        filters=github_graphene.GHSearchRequestInput(),
    )

    @staticmethod
    def resolve_search(parent, info, filters):
        return github_service.search(
            github_pydantic.GHSearchRequest(**filters),
            "GraphQL",
        )


schema = graphene.Schema(query=Query)

app.add_route(
    "/GraphQL",
    starlette_graphene3.GraphQLApp(
        schema=schema,
        on_get=starlette_graphene3.make_graphiql_handler(),
    ),
)
