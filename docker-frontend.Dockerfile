FROM node:17

RUN npm i http-server -g

WORKDIR /src/frontend

COPY ./proto /src/proto
COPY ./frontend /src/frontend
COPY ./_utils/js-build.sh /usr/local/bin/js-build
COPY ./_utils/proto-build-js.sh /usr/local/bin/proto-build-js

RUN apt-get update \
    && apt-get install -y wget protobuf-compiler \
    && wget https://github.com/grpc/grpc-web/releases/download/1.3.1/protoc-gen-grpc-web-1.3.1-linux-x86_64 --output-document=/usr/local/bin/protoc-gen-grpc-web \
    && chmod +x /usr/local/bin/protoc-gen-grpc-web

CMD /usr/local/bin/proto-build-js \
    && /usr/local/bin/js-build \
    && http-server -a --port=8081