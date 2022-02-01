import github_pydantic
import graphene
import pydantic2graphene


class GHSearchRequest(
    pydantic2graphene.to_graphene(github_pydantic.GHSearchRequest)
):
    pass


class GHSearchRequestInput(
    pydantic2graphene.to_graphene(
        github_pydantic.GHSearchRequest, graphene.InputObjectType
    )
):
    pass


class GHSearchResponse(
    pydantic2graphene.to_graphene(github_pydantic.GHSearchResponse)
):
    pass
