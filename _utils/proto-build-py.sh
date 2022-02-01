#!/bin/bash

python -m grpc_tools.protoc \
    /src/proto/github.proto \
    --proto_path=/src/proto/ \
    --python_out=/src/backend/ \
    --grpc_python_out=/src/backend/