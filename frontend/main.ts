import { GHSearchRequest } from './github_pb';
import * as client_grpc from './client_grpc';
import * as client_rest from './client_rest';

const grpcText = document.getElementById("client_grpc") as HTMLTextAreaElement;
const restText = document.getElementById("client_rest") as HTMLTextAreaElement;

const appendText = (element: HTMLTextAreaElement, text: string) => {
    element.value += text + "\n";
}

const request = new GHSearchRequest();
request.setQuery("This is a test query");
request.setType(GHSearchRequest.QueryType.REPO);
request.setResultPerPage(10);

appendText(restText, "Start REST request ...");
client_rest.search(request).then((response) => {
    appendText(restText, `Complete: ${JSON.stringify(response.toObject())}`)
})

appendText(grpcText, "Start gRCP request ...");
client_grpc.search(request).then((response) => {
    appendText(grpcText, `Complete: ${JSON.stringify(response.toObject())}`)
})

