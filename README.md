# protobuf-to-server

Project to explore [Protocol Buffers](https://developers.google.com/protocol-buffers) to empower a [gRPC](https://grpc.io/), [REST API](https://restfulapi.net/) and [GraphQL](https://graphql.org/) in the backend and a [gRPC web client](https://github.com/grpc/grpc-web) in the frontend, all trhee backends and the frontend are using the same proto definition, they are just compiled in different languages or converted to some frameworks specific objects, but all use the `proto` as primary data model.

## Proto definition

```proto
message GHSearchRequest {
    string query = 1;
    enum QueryType {
        UNKNOWN = 0;
        USER = 1;
        REPO = 2;
    }
    QueryType type = 2;
    int32 result_per_page = 3;
}

message GHSearchResponse {
    string server_response = 1;
    GHSearchRequest.QueryType type = 2;
}

service GithubService {
    rpc Search(GHSearchRequest) returns (GHSearchResponse);
}
```

## UI

![image](https://user-images.githubusercontent.com/45940140/152046684-b6c33ec4-c3c5-4779-ba1e-888ed12f611b.png)

- REST API playground is available at `/rest/docs`

![image](https://user-images.githubusercontent.com/45940140/152047274-8a4ef374-6a6b-44d5-9d9f-aa91ddf7987e.png)

- GraphQL playgroud is available at `/GraphQL`


![image](https://user-images.githubusercontent.com/45940140/152047619-ed5cc57e-dd1c-4330-a195-509639004671.png)

## Running the project

    docker-compose up --build -d

Docker compose will compile the `protos` and `ts` and then start the server, once the containers are running you should be able to access the UIs at http://localhost:8080 (*Note: the home page `/`  sometimes take longer to be available, if home not loading try refresh the page, if that doens't work `docker-compose restart`*)