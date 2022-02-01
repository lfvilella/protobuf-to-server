#!/bin/bash

protoc /src/proto/github.proto \
    --proto_path=/src/proto \
    --js_out=import_style=commonjs,binary:/src/frontend/ \
    --grpc-web_out=import_style=typescript,mode=grpcweb:/src/frontend/
