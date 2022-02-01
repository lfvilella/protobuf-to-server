const {GHSearchRequest, GHSearchResponse} = require('./github_pb.js');
const {GithubServiceClient} = require('./github_grpc_web_pb.js');

var client = new GithubServiceClient('http://localhost:8080');

var request = new GHSearchRequest();
request.setQuery("q1");
request.setType(GHSearchRequest.QueryType.USER);
request.setResultPerPage(10);

client.search(request, {}, (err, response) => {
  console.log(response.getType(), response.getServerResponse());
});