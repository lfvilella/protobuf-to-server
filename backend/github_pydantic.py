import github_pb2
import protobuf2pydantic
import pydantic


class CamelBaseModel(pydantic.BaseModel):
    class Config:
        def _camel(obj: str) -> str:
            _str = "".join(map(str.capitalize, obj.split("_")))
            return _str[0].lower() + _str[1:]

        alias_generator = _camel
        allow_population_by_field_name = True


class GHSearchRequest(
    CamelBaseModel, protobuf2pydantic.msg2py(github_pb2.GHSearchRequest)
):
    pass


class GHSearchResponse(
    CamelBaseModel, protobuf2pydantic.msg2py(github_pb2.GHSearchResponse)
):
    pass
