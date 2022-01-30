import protobuf2pydantic

import github_pb2


class GHSearchRequest(protobuf2pydantic.msg2py(github_pb2.GHSearchRequest)):
    pass


class GHSearchResponse(protobuf2pydantic.msg2py(github_pb2.GHSearchResponse)):
    pass
