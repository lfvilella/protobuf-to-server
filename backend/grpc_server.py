import logging
from concurrent import futures

import github_pb2
import github_pb2_grpc
import github_pydantic
import grpc
from google.protobuf import json_format
from grpc.reflection.v1alpha import reflection
from services import github_service


class GithubService(github_pb2_grpc.GithubServiceServicer):
    def Search(
        self,
        request: github_pb2.GHSearchRequest,
        context: grpc.ServicerContext,
    ) -> github_pb2.GHSearchResponse:
        dict_request = json_format.MessageToDict(
            request,
            preserving_proto_field_name=True,
            use_integers_for_enums=True,
        )
        py_request = github_pydantic.GHSearchRequest(**dict_request)
        py_response = github_service.search(py_request, "gRPC")
        return github_pb2.GHSearchResponse(**py_response.dict())


def serve():
    service_names = []
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    logging.info("Attaching GithubService")
    github_pb2_grpc.add_GithubServiceServicer_to_server(
        GithubService(),
        server,
    )
    service_names.append(
        github_pb2.DESCRIPTOR.services_by_name["GithubService"].full_name
    )

    service_names.append(reflection.SERVICE_NAME)
    reflection.enable_server_reflection(service_names, server)

    server_port = "[::]:8001"
    server.add_insecure_port(server_port)
    logging.info("Starting gRPC server: %s", server_port)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve()
