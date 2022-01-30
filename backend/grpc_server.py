import logging
from concurrent import futures

import grpc

import github_pb2
import github_pb2_grpc
import github_pydantic
from services import github_service


class GithubService(github_pb2_grpc.GithubServiceServicer):
    def Search(
        self,
        request: github_pb2.GHSearchRequest,
        context: grpc.ServicerContext,
    ) -> github_pb2.GHSearchResponse:
        py_request = github_pydantic.GHSearchRequest(
            query=request.query,
            type=request.type,
            result_per_page=request.result_per_page,
        )
        py_response = github_service.search(py_request)
        return github_pb2.GHSearchResponse(**py_response.dict())


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    github_pb2_grpc.add_GithubServiceServicer_to_server(
        GithubService(),
        server,
    )
    server.add_insecure_port("[::]:50051")
    logging.info("Starting gRPC server")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve()
