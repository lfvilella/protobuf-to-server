FROM python:3.10

# RUN pip install --upgrade pip \
#     pip install grpcio grpcio-tools

# docker run --rm -it -p 8000:8000 -p 50051:50051 -v $(pwd):/app -w /app python:3.10 /bin/bash
# python -m grpc_tools.protoc /app/proto/github.proto --proto_path=/app/proto/ --python_out=/app/backend/ --grpc_python_out=/app/backend/
# uvicorn http_server:app --reload --host=0.0.0.0 --port=8000
