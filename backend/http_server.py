import fastapi
import graphene
import pydantic.error_wrappers
import starlette_graphene3
from fastapi import exception_handlers

import github_graphene
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


class Query(graphene.ObjectType):
    search = graphene.Field(
        github_graphene.GHSearchResponse,
        filters=github_graphene.GHSearchRequestInput(),
    )

    @staticmethod
    def resolve_search(parent, info, filters):
        return github_service.search(
            github_pydantic.GHSearchRequest(**filters)
        )


schema = graphene.Schema(query=Query)

app.add_route(
    "/graphql",
    starlette_graphene3.GraphQLApp(
        schema=schema,
        on_get=starlette_graphene3.make_graphiql_handler(),
    ),
)
