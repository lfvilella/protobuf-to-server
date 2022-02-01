#!/bin/bash

protoc /src/proto/github.proto \
    --proto_path=/src/proto --js_out=import_style=commonjs:/src/frontend/ --grpc-web_out=import_style=commonjs,mode=grpcwebtext:/src/frontend/