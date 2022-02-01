import { GHSearchRequest } from './github_pb';
import * as client_grpc from './client_grpc';
import * as client_rest from './client_rest';
import * as client_graphql from './client_graphql';

const grpcText = document.getElementById("client_grpc") as HTMLTextAreaElement;
const restText = document.getElementById("client_rest") as HTMLTextAreaElement;
const grapthqlText = document.getElementById("client_graphql") as HTMLTextAreaElement;

const appendText = (element: HTMLTextAreaElement, text: string) => {
    element.value += text + "\n";
}

const request = new GHSearchRequest();
request.setQuery("This is a test query");
request.setType(GHSearchRequest.QueryType.REPO);
request.setResultPerPage(10);

appendText(grpcText, "Start gRCP request ...");
client_grpc.search(request).then((response) => {
    appendText(grpcText, `Complete: ${JSON.stringify(response.toObject())}`)
})

appendText(restText, "Start REST request ...");
client_rest.search(request).then((response) => {
    appendText(restText, `Complete: ${JSON.stringify(response.toObject())}`)
})

appendText(grapthqlText, "Start GraphQL request ...");
client_graphql.search(request).then((response) => {
    appendText(grapthqlText, `Complete: ${JSON.stringify(response.toObject())}`)
})
